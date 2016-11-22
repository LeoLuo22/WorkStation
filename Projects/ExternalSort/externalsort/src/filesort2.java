package externalsort;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;
import java.util.Spliterator;

public class filesort {
	public static int ITEM_COUNT = 1000000;
	public static int BUFFER_SIZE = 1024 * 4 * 1024; //缓冲大小，这里设为4mB
	public static int FILE_COUNT = 5000;//1024 * 1000 * 1 * 4;// 文件分割后每个文件的记录数
	public static File MAIN_FILE = new File("D:/unsorted1.txt");

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		filesort sort = new filesort();
		System.out.println("Original: ");

		long start = System.currentTimeMillis();
		sort.mSort(MAIN_FILE);

		long end = System.currentTimeMillis();
		System.out.println((end - start) / 1000 + "s");
		recordFile((end - start) / 1000, true);
	}

	private static void recordFile(long time, boolean isBuffer) throws FileNotFoundException, IOException {
		BufferedWriter bw = new BufferedWriter(new FileWriter("log", true));
		bw.write("FILE_COUNT = " + FILE_COUNT + ";对" + ITEM_COUNT + "条数据" + ITEM_COUNT * 4 / (1024 * 1024) + "MB排序耗时: "
				+ time + "s ");
		if (isBuffer)
			bw.write("使用缓冲" + BUFFER_SIZE * 4 / (1024 * 1024) + "MB");
		bw.newLine();
		bw.close();
	}

	/*
	 * 多路归并
	 */
	public void mSort(File file) throws IOException {
		ArrayList<File> files = split(file);
		multipleMerge(files);
	}

	/*
	 * 分割文件
	 */
	private ArrayList<File> split(File file) throws IOException {
		ArrayList<File> files = new ArrayList<File>();
		ArrayList<String> buffer = new ArrayList<String>();
		//String[] buffer = new String[FILE_COUNT];
		FileInputStream fr = new FileInputStream(file);
		// BUFFER_SIZE提供缓冲区大小
		BufferedInputStream bin = new BufferedInputStream(fr, BUFFER_SIZE);
		BufferedReader din = new BufferedReader(new InputStreamReader(bin));
		boolean fileComplete = false;

		while (!fileComplete) {
			int index = buffer.length;
			for (int i = 0; i < buffer.length && !fileComplete; ++i) {
				try {
					buffer[i] = din.readLine();
				} catch (Exception e) {
					// TODO: handle exception
					fileComplete = true;
					index = i;
				}
			}
			/*
			 * debug
			 */
			/*
			for(String string : buffer)
				System.out.println(string);
				*/
			
			if (index != 0 && buffer[0] != null) {
				// 从buffer的起始位到结束位排序
				try{
				Arrays.sort(buffer);//, 0, index);
				}catch (NullPointerException e) {
					// TODO: handle exception
					System.out.println(buffer.length);
					String[] newbuffer = new String[buffer.length];
					System.out.println("sort err");
				}
				File f = new File("set" + new Random().nextInt());
				FileWriter fileWriter = new FileWriter(f, true);
				BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
				for (int j = 0; j < index; ++j) {
					// 写入文件
					try{
					if(buffer[j] != null)
					{
					bufferedWriter.write(buffer[j]);
					bufferedWriter.newLine();
					}
					else
						break;
					}catch (NullPointerException e) {
						// TODO: handle exception
						//System.out.println("拆分即将完成");
						j = index;
						System.out.println("write err");
					}
				}
				bufferedWriter.close();
				files.add(f);
			}
			
			
		}
		din.close();
		bin.close();
		fr.close();
		System.out.println("Total:" + files.size());
		return files;
	}

	/*
	 * 多路归并
	 */
	private void multipleMerge(ArrayList<File> list) throws IOException {
		int fileSize = list.size();

		// 判断归并是否完成
		if (fileSize == 1) {
			return;
		}

		ArrayList<DataInputStream> dinlist = new ArrayList<DataInputStream>();

		String[] ext = new String[fileSize];// 比较数组

		FileOutputStream os = new FileOutputStream(MAIN_FILE);
		BufferedOutputStream bout = new BufferedOutputStream(os);
		DataOutputStream dout = new DataOutputStream(bout);

		for (int i = 0; i < fileSize; ++i) {
			try {
				dinlist.add(i,
						new DataInputStream(new BufferedInputStream(new FileInputStream(list.get(i)), BUFFER_SIZE)));

			} catch (Exception e) {
				// TODO: handle exception
				e.printStackTrace();
			}
		}
		int index = 0;

		for (int i = 0; i < fileSize; ++i) {
			try {
				ext[i] = dinlist.get(i).readLine();
			} catch (Exception e) {
				// TODO: handle exception
				System.out.println("file_" + i + "为空");
				ext[i] = "";
			}
		}
		int count = fileSize;
		int[] sum = new int[fileSize];

		while (count > 1) {

			index = getMinIndex(ext);
			dout.writeChars(ext[index]);
			sum[index]++;
			try {
				ext[index] = dinlist.get(index).readLine();
			} catch (Exception e) {
				// TODO: handle exception
				ext[index] = "";
				count--;
				dinlist.get(index).close();
			}
		}
		int sIndex = getSIndex(ext);
		// what
		dout.writeChars(ext[sIndex]);
		while (true) {
			try {
				dout.writeChars(dinlist.get(sIndex).readLine());
			} catch (Exception e) {
				dinlist.get(sIndex).close();
				break;
			}
		}
		dout.close();
	}

	// 找到最后的一个文件输入流
	public int getSIndex(String[] ext) {
		int result = 0;
		for (int i = 0; i < ext.length; ++i) {
			if (ext[i] != "") {
				result = i;
				break;
			}
		}
		return result;
	}

	// 找到数据中最小的一个
	public int getMinIndex(String[] ext) {
		String min = "{";
		int index = -1;
		for (int i = 0; i < ext.length; ++i) {
			if (ext[i] != "" && ext[i].compareTo(min) < 0) {
				min = ext[i];
				index = i;
			}

		}
		return index;
	}

}
