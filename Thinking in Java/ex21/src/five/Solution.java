package five;

public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i = 0; i <= 100; ++i) {
			Thread thread = new Thread(new Fib(i));
			thread.start();
		}

	}

}

class Fib implements Runnable {
	private int n = 0;

	private int fibonacci(int n) {
		if (n == 0)
			return 0;
		if (n == 1)
			return 1;
		return fibonacci(n - 1) + fibonacci(n - 2);

	}

	public Fib(int n) {
		this.n = n;
	}

	public void run() {
		for (int i = 0; i <= n; ++i) {
			System.out.println(this.fibonacci(i));
			Thread.yield();
		}
	}
}