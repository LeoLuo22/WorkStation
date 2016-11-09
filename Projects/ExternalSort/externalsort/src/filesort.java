import java.io.*;
import java.util.*;
import org.apache.commons.io.*;

public class filesort {
	private filesort() {
	}

	/**
	 * 得到指定文件的行数
	 * 
	 * @param fileC
	 *            String
	 * @return int
	 * @throws IOException
	 */
	private static int getFileLineSize(String fileC) throws IOException {
		Reader fC = null;
		try {
			fC = new FileReader(fileC);

			LineIterator it = IOUtils.lineIterator(fC);
			int lineSize = 0;
			while (it.hasNext()) {
				it.nextLine();
				lineSize++;
			}
			return lineSize;
		} finally {
			IOUtils.closeQuietly(fC);
		}
	}

	/**
	 * 得到下一行的内容,如果已到文件末尾返回NULL
	 * 
	 * @param iterator
	 *            LineIterator
	 * @return String
	 */
	private static String nextLine(LineIterator iterator) {
		if (iterator.hasNext()) {
			return iterator.nextLine();
		} else {
			return null;
		}
	}

	/**
	 * 读指定行数的字符串到缓冲区列表里
	 * 
	 * @param iterator
	 *            LineIterator
	 * @param bufList
	 *            List
	 * @param lines
	 *            int
	 */
	private static void readLines(LineIterator iterator, List<String> bufList, int lines) {
		for (int i = 0; i < lines; i++) {
			if (!iterator.hasNext()) {
				break;
			}
			bufList.add(iterator.nextLine());
		}
	}

	/**
	 * 扫描fileC中的归并段并把它们交替分别送到文件fileA和fileB中, 本次归并段的大小为k*blockSize
	 * 
	 * @param fileA
	 *            String
	 * @param fileB
	 *            String
	 * @param fileC
	 *            String
	 * @param k
	 *            int
	 * @param blockSize
	 *            int
	 */
	private static void split(String fileA, String fileB, String fileC, int k, int blockSize)
			throws FileNotFoundException, IOException {
		boolean useA = true;
		int i = 0;

		List<String> bufList = new ArrayList<String>(blockSize); // 大小为blockSize的缓冲区
		Writer fA = null;
		Writer fB = null;
		Reader fC = null;
		try {
			fA = new BufferedWriter(new FileWriter(fileA));
			fB = new BufferedWriter(new FileWriter(fileB));
			fC = new FileReader(fileC);

			LineIterator itC = IOUtils.lineIterator(fC);
			while (itC.hasNext()) {
				// ->读入数据块
				bufList.clear();
				readLines(itC, bufList, blockSize);
				// <-读入数据块

				if (useA) {
					IOUtils.writeLines(bufList, "\n", fA);
				} else {
					IOUtils.writeLines(bufList, "\n", fB);
				}

				if (++i == k) {
					i = 0;
					useA = !useA;
				}
			}
		} finally {
			bufList.clear();

			IOUtils.closeQuietly(fA);
			IOUtils.closeQuietly(fB);
			IOUtils.closeQuietly(fC);
		}
	}

	/**
	 * n为当前归并段大小(k*blockSize);将文件fX的后续归并段拷入到fY,变量currRunPos为当前归并段的索引
	 * 
	 * @param fileX
	 *            String
	 * @param fileY
	 *            String
	 * @param currRunPos
	 *            int
	 * @param n
	 *            int
	 * @return int 当前归并段的索引
	 */
	private static int copyTail(LineIterator fileX, Writer fileY, int currRunPos, int n) throws IOException {
		// 从当前位置到归并段结束,拷贝每个数据
		while (currRunPos <= n) {
			// 若没有更多的数据项,则文件结束且归并段结束
			if (!fileX.hasNext()) {
				break;
			}

			// 修改当前归并段位置并将数据项写入fY
			currRunPos++;
			IOUtils.write(fileX.nextLine() + "\n", fileY);
		}

		return currRunPos;
	}

	/**
	 * 将文件fA和fB中长度为n(k*blockSize)的归并段合并回fC中
	 * 
	 * @param fileA
	 *            String
	 * @param fileB
	 *            String
	 * @param fileC
	 *            String
	 * @param n
	 *            int
	 * @throws IOException
	 */
	private static void merge(String fileA, String fileB, String fileC, int n) throws IOException {
		// currA和currB表示在当前归并段中的位置
		int currA = 1;
		int currB = 1;

		// 分别从fA和fB中读出的数据项
		String dataA, dataB;

		Reader fA = null;
		Reader fB = null;
		Writer fC = null;
		try {
			fA = new FileReader(fileA);
			fB = new FileReader(fileB);
			fC = new BufferedWriter(new FileWriter(fileC));

			LineIterator itA = IOUtils.lineIterator(fA);
			LineIterator itB = IOUtils.lineIterator(fB);

			dataA = nextLine(itA);
			dataB = nextLine(itB);
			for (;;) {
				// 若(dataA<=dataB),则将dataA拷贝到fC并修改当前归并段的位置
				if (dataA.compareTo(dataB) <= 0) {
					IOUtils.write(dataA + "\n", fC);

					// 从fA中取下一归并段,若不存在,则已到文件尾,应将fB的后续归并段拷入到fC;
					// 若当前位置>n,则已将所有fA的归并段拷完,应拷贝fB的后续归并段
					dataA = nextLine(itA);
					currA++;
					if (dataA == null || currA > n) {
						IOUtils.write(dataB + "\n", fC);
						currB++;
						currB = copyTail(itB, fC, currB, n);

						// fA的大小>=fB的大小;若在fA的文件尾,则结束
						if (dataA == null) {
							break;
						} else { // 否则,应在新的归并段中,重置当前位置
							currA = 1;
						}

						// 取fB中的下一项.若不存在,则只有fA中剩余的部分要拷贝到fC,
						// 退出循环前将当前归并段写入fC
						dataB = nextLine(itB);
						if (dataB == null) {
							IOUtils.write(dataA + "\n", fC);
							currA = 2;
							break;
						} else { // 否则,重置fB中当前归并段
							currB = 1;
						}
					}
				} else { // 否则(dataA>dataB)
					IOUtils.write(dataB + "\n", fC);

					// 从fB中取下一归并段,若不存在,则已到文件尾,应将fA的后续归并段拷入到fC;
					// 若当前位置>n,则已将所有fB的归并段拷完,应拷贝fA的后续归并段
					dataB = nextLine(itB);
					currB++;
					if (dataB == null || currB > n) {
						IOUtils.write(dataA + "\n", fC);
						currA++;
						currA = copyTail(itA, fC, currA, n);

						// 若fB中没有更多项,则置fA的当前位置,准备拷贝fA中的最后归并段到fC中
						if (dataB == null) {
							currA = 1;
							break;
						} else { // 否则,置fB的当前位置,并从fA中读入数据
							currB = 1;
							if ((dataA = nextLine(itA)) == null) {
								break;
							} else {
								currA = 1;
							}
						}
					}
				}
			} // <- end for(; ;)

			// 将fA中可能存在的剩余的归并段写入fC中(注:fA的长度时>=fB的)
			if (dataA != null && dataB == null) {
				currA = copyTail(itA, fC, currA, n);
			}
		} finally {
			IOUtils.closeQuietly(fA);
			IOUtils.closeQuietly(fB);
			IOUtils.closeQuietly(fC);
		}
	}

	/**
	 * 用指定的blockSize块大小,排序指定的文件fileC
	 * 
	 * @param fileC
	 *            String
	 * @param blockSize
	 *            int
	 * @throws IOException
	 */

	/**
	 * 用指定的blockSize块大小,排序指定的文件fileSource,排序后的文件是fileOut
	 * 
	 * @param fileSource
	 *            String
	 * @param fileOut
	 *            String
	 * @param blockSize
	 *            int
	 * @param removeDuple
	 * @throws IOException
	 */
	public static void sort(String fileSource, String fileOut, int blockSize) throws IOException {
		String fileA = File.createTempFile("wjw", null).getAbsolutePath();
		String fileB = File.createTempFile("wjw", null).getAbsolutePath();

		int mergeIndex = 1;
		int lineSize = getFileLineSize(fileSource);
		int k = 1;
		int n = k * blockSize;
		boolean useA = true;
		List<String> list = new ArrayList<String>(blockSize);

		Writer fA = null;
		Writer fB = null;
		Reader fC = null;
		try {
			fA = new BufferedWriter(new FileWriter(fileA));
			fB = new BufferedWriter(new FileWriter(fileB));
			fC = new FileReader(fileSource);

			LineIterator itC = IOUtils.lineIterator(fC);
			if (lineSize <= blockSize) { // 对于小文件,从fC读入数据,直接排序后写回文件中
				readLines(itC, list, lineSize);
				Collections.sort(list);
				IOUtils.closeQuietly(fC);
				FileUtils.writeLines(new File(fileOut), "GBK", list, "\n");

				list.clear();
				return;
			}

			// ->第一次分割,合并
			// System.out.println("第:"+mergeIndex+"分割,合并");
			while (itC.hasNext()) {
				list.clear();
				readLines(itC, list, blockSize);

				Collections.sort(list);
				if (useA) {
					IOUtils.writeLines(list, "\n", fA);
				} else {
					IOUtils.writeLines(list, "\n", fB);
				}

				useA = !useA;
			}
			list.clear();

			IOUtils.closeQuietly(fA);
			IOUtils.closeQuietly(fB);
			IOUtils.closeQuietly(fC);
			merge(fileA, fileB, fileOut, blockSize);
			mergeIndex++;
			// <-第一次分割,合并

			// ->将当前归并段大小加倍,循环进行
			k = k * 2;
			n = k * blockSize;
			while (n < lineSize) { // 当n>=文件大小时,fC仅剩一个已排好序的归并段
				// System.out.println("第:"+mergeIndex+"分割,合并");
				split(fileA, fileB, fileOut, k, blockSize);
				merge(fileA, fileB, fileOut, n);
				mergeIndex++;
				k = k * 2;
				n = k * blockSize;
			}
			// ->将当前归并段大小加倍,循环进行

		} finally {
			IOUtils.closeQuietly(fA);
			IOUtils.closeQuietly(fB);
			IOUtils.closeQuietly(fC);

			(new File(fileA)).delete();
			(new File(fileB)).delete();
		}
	}

	/**
	 * 删除已经排好序的文件中重复的数据
	 * 
	 * @param fileC
	 *            String
	 * @throws IOException
	 */
	public static String formatSecond(long seconds) {
		long h = seconds / (60 * 60);
		StringBuffer sb = new StringBuffer();

		sb.append(h + "小时");

		seconds = seconds % (60 * 60);

		long c = seconds / 60;
		sb.append(c + "分");

		sb.append(seconds % 60 + "秒");

		return sb.toString();
	}
	
	public static void union(String[] paths, String newString)throws Exception  
    {  
        File[] list = new File[paths.length];
        for(int i = 0; i < paths.length; ++i){
        	list[i] = new File(paths[i]);
        }
        File newFile=new File(newString);  
        byte buffer[]=new byte[1024];  
        int readcount; 
        /*
        if(!newFile.getParentFile().exists())  
            throw new Exception("你合并的文件夹的不存在...");  
            */
        FileOutputStream writer=new FileOutputStream(newString);  
        for(File f:list)  
        {  
            FileInputStream reader=new FileInputStream(f);  
            while((readcount=reader.read(buffer))!=-1)  
            {  
                writer.write(buffer);  
            }  
            reader.close();  
        }  
        writer.close();  
    }  

	public static void main(String args[]) {
		//System.out.println("Usage: filesort INPUT_FILE_1 INPUT_FILE_2 ... OUTPUT_FILE");
		long c1 = System.currentTimeMillis();
		String[] input_files = new String[args.length - 1];
		for(int i = 0; i < args.length - 1; ++i)
			input_files[i] = args[i];
		try {
			union(input_files, "merged.txt");
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		String output = args[args.length - 1];
		int blockSize = 1000;
		try {
			filesort.sort("merged.txt", output, blockSize);
			long c2 = (System.currentTimeMillis() - c1) / 1000;
			System.out.println("Generate sorted file: " + output);
			System.out.println("耗时:" + formatSecond(c2));
			long total = Runtime.getRuntime().totalMemory();
			long free = Runtime.getRuntime().freeMemory();
			System.out.println("Used memory: " + (total - free) + "B" + "(" + (total - free) / 1024 / 1024 + "MB" + ")");
		} catch (IOException ex) {
			ex.printStackTrace();
		}
	}

}