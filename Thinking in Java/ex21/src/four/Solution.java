package four;

public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		while (true) {
			Thread thread = new Thread(new MultiProcess());
			thread.start();
			System.out.println("Waiting");
		}

	}

}

class MultiProcess implements Runnable {
	private int count = 3;

	public MultiProcess() {
		System.out.println("Start");
	}

	public void run() {
		while (count-- > 0) {
			System.out.println("hello, world" + count);
			Thread.yield();
		}
		System.out.println("End");
	}
}