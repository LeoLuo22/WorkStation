import java.io.BufferedWriter;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class filesort_testgen {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int filecount = 0;
		long line = 0;
		String prefix = "";
		while(true){
			try{
				filecount = Integer.parseInt(args[0]);
				line = Long.parseLong(args[1]);
				prefix = args[2];
				break;
			}catch (NumberFormatException e) {
				// TODO: handle exception
				System.out.println("Wrong input, try again...");
				return;
			}
		}
		Random random = new Random();
		System.out.println("Generate unsorted files: ");
		for (int j = 1; j < filecount + 1; ++j) {
			double size = (1024 * 1024 * 1024) * (1 + Math.random());
			double bytes = size / line;
			String filename = "";
			try {

				/*
				 * @ generate file
				 */
				filename = prefix + j;
				System.out.println(filename);
				File file = new File(filename + ".txt");
				if (!file.exists())
					file.createNewFile();
				FileWriter fileWriter = new FileWriter(file.getName(), true);
				BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

				for (long i = 0; i < line + random.nextInt(1000); ++i) {
					bufferedWriter.write(getRandomString(bytes));
					bufferedWriter.newLine();
				}
				bufferedWriter.close();
			} catch (IOException e) {
				// TODO: handle exception
				e.printStackTrace();
			}
		}

	}

	public static String getRandomString(double bytes) {
		String str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
		Random random = new Random();
		StringBuffer sb = new StringBuffer();
		for (int i = 0; i < bytes; i++) {
			int number = random.nextInt(62);
			sb.append(str.charAt(number));
		}
		return sb.toString();
	}

}
