import java.io.*;
import java.util.*;
import org.apache.commons.io.*;

public class filesort {
	private filesort() {
	}

	/**
	 * �õ�ָ���ļ�������
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
	 * �õ���һ�е�����,����ѵ��ļ�ĩβ����NULL
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
	 * ��ָ���������ַ������������б���
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
	 * ɨ��fileC�еĹ鲢�β������ǽ���ֱ��͵��ļ�fileA��fileB��, ���ι鲢�εĴ�СΪk*blockSize
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

		List<String> bufList = new ArrayList<String>(blockSize); // ��СΪblockSize�Ļ�����
		Writer fA = null;
		Writer fB = null;
		Reader fC = null;
		try {
			fA = new BufferedWriter(new FileWriter(fileA));
			fB = new BufferedWriter(new FileWriter(fileB));
			fC = new FileReader(fileC);

			LineIterator itC = IOUtils.lineIterator(fC);
			while (itC.hasNext()) {
				// ->�������ݿ�
				bufList.clear();
				readLines(itC, bufList, blockSize);
				// <-�������ݿ�

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
	 * nΪ��ǰ�鲢�δ�С(k*blockSize);���ļ�fX�ĺ����鲢�ο��뵽fY,����currRunPosΪ��ǰ�鲢�ε�����
	 * 
	 * @param fileX
	 *            String
	 * @param fileY
	 *            String
	 * @param currRunPos
	 *            int
	 * @param n
	 *            int
	 * @return int ��ǰ�鲢�ε�����
	 */
	private static int copyTail(LineIterator fileX, Writer fileY, int currRunPos, int n) throws IOException {
		// �ӵ�ǰλ�õ��鲢�ν���,����ÿ������
		while (currRunPos <= n) {
			// ��û�и����������,���ļ������ҹ鲢�ν���
			if (!fileX.hasNext()) {
				break;
			}

			// �޸ĵ�ǰ�鲢��λ�ò���������д��fY
			currRunPos++;
			IOUtils.write(fileX.nextLine() + "\n", fileY);
		}

		return currRunPos;
	}

	/**
	 * ���ļ�fA��fB�г���Ϊn(k*blockSize)�Ĺ鲢�κϲ���fC��
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
		// currA��currB��ʾ�ڵ�ǰ�鲢���е�λ��
		int currA = 1;
		int currB = 1;

		// �ֱ��fA��fB�ж�����������
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
				// ��(dataA<=dataB),��dataA������fC���޸ĵ�ǰ�鲢�ε�λ��
				if (dataA.compareTo(dataB) <= 0) {
					IOUtils.write(dataA + "\n", fC);

					// ��fA��ȡ��һ�鲢��,��������,���ѵ��ļ�β,Ӧ��fB�ĺ����鲢�ο��뵽fC;
					// ����ǰλ��>n,���ѽ�����fA�Ĺ鲢�ο���,Ӧ����fB�ĺ����鲢��
					dataA = nextLine(itA);
					currA++;
					if (dataA == null || currA > n) {
						IOUtils.write(dataB + "\n", fC);
						currB++;
						currB = copyTail(itB, fC, currB, n);

						// fA�Ĵ�С>=fB�Ĵ�С;����fA���ļ�β,�����
						if (dataA == null) {
							break;
						} else { // ����,Ӧ���µĹ鲢����,���õ�ǰλ��
							currA = 1;
						}

						// ȡfB�е���һ��.��������,��ֻ��fA��ʣ��Ĳ���Ҫ������fC,
						// �˳�ѭ��ǰ����ǰ�鲢��д��fC
						dataB = nextLine(itB);
						if (dataB == null) {
							IOUtils.write(dataA + "\n", fC);
							currA = 2;
							break;
						} else { // ����,����fB�е�ǰ�鲢��
							currB = 1;
						}
					}
				} else { // ����(dataA>dataB)
					IOUtils.write(dataB + "\n", fC);

					// ��fB��ȡ��һ�鲢��,��������,���ѵ��ļ�β,Ӧ��fA�ĺ����鲢�ο��뵽fC;
					// ����ǰλ��>n,���ѽ�����fB�Ĺ鲢�ο���,Ӧ����fA�ĺ����鲢��
					dataB = nextLine(itB);
					currB++;
					if (dataB == null || currB > n) {
						IOUtils.write(dataA + "\n", fC);
						currA++;
						currA = copyTail(itA, fC, currA, n);

						// ��fB��û�и�����,����fA�ĵ�ǰλ��,׼������fA�е����鲢�ε�fC��
						if (dataB == null) {
							currA = 1;
							break;
						} else { // ����,��fB�ĵ�ǰλ��,����fA�ж�������
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

			// ��fA�п��ܴ��ڵ�ʣ��Ĺ鲢��д��fC��(ע:fA�ĳ���ʱ>=fB��)
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
	 * ��ָ����blockSize���С,����ָ�����ļ�fileC
	 * 
	 * @param fileC
	 *            String
	 * @param blockSize
	 *            int
	 * @throws IOException
	 */

	/**
	 * ��ָ����blockSize���С,����ָ�����ļ�fileSource,�������ļ���fileOut
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
			if (lineSize <= blockSize) { // ����С�ļ�,��fC��������,ֱ�������д���ļ���
				readLines(itC, list, lineSize);
				Collections.sort(list);
				IOUtils.closeQuietly(fC);
				FileUtils.writeLines(new File(fileOut), "GBK", list, "\n");

				list.clear();
				return;
			}

			// ->��һ�ηָ�,�ϲ�
			// System.out.println("��:"+mergeIndex+"�ָ�,�ϲ�");
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
			// <-��һ�ηָ�,�ϲ�

			// ->����ǰ�鲢�δ�С�ӱ�,ѭ������
			k = k * 2;
			n = k * blockSize;
			while (n < lineSize) { // ��n>=�ļ���Сʱ,fC��ʣһ�����ź���Ĺ鲢��
				// System.out.println("��:"+mergeIndex+"�ָ�,�ϲ�");
				split(fileA, fileB, fileOut, k, blockSize);
				merge(fileA, fileB, fileOut, n);
				mergeIndex++;
				k = k * 2;
				n = k * blockSize;
			}
			// ->����ǰ�鲢�δ�С�ӱ�,ѭ������

		} finally {
			IOUtils.closeQuietly(fA);
			IOUtils.closeQuietly(fB);
			IOUtils.closeQuietly(fC);

			(new File(fileA)).delete();
			(new File(fileB)).delete();
		}
	}

	/**
	 * ɾ���Ѿ��ź�����ļ����ظ�������
	 * 
	 * @param fileC
	 *            String
	 * @throws IOException
	 */
	public static String formatSecond(long seconds) {
		long h = seconds / (60 * 60);
		StringBuffer sb = new StringBuffer();

		sb.append(h + "Сʱ");

		seconds = seconds % (60 * 60);

		long c = seconds / 60;
		sb.append(c + "��");

		sb.append(seconds % 60 + "��");

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
            throw new Exception("��ϲ����ļ��еĲ�����...");  
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
			System.out.println("��ʱ:" + formatSecond(c2));
			long total = Runtime.getRuntime().totalMemory();
			long free = Runtime.getRuntime().freeMemory();
			System.out.println("Used memory: " + (total - free) + "B" + "(" + (total - free) / 1024 / 1024 + "MB" + ")");
		} catch (IOException ex) {
			ex.printStackTrace();
		}
	}

}