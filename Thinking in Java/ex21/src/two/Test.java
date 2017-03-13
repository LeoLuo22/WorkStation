package two;

import static com.leoluo.util.Print.*;

import java.util.concurrent.TimeUnit;

class Daemon implements Runnable {
	private Thread[] threads = new Thread[10];

	public void run() {
		for (int i = 0; i < threads.length; ++i) {
			threads[i] = new Thread(new DaemonSpawn());
			threads[i].start();
			printnb("DaemonSpawn " + i + " started. ");
		}
		for (int i = 0; i < threads.length; ++i)
			printnb("t[" + i + "].isDaemon() = " + threads[i].isDaemon() + ". ");
		while (true)
			Thread.yield();
	}
}
class DaemonSpawn implements Runnable{
	public void run(){
		while(true)
			Thread.yield();
	}
}
public class Test {

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
		Thread thread = new Thread(new Daemon());
		thread.setDaemon(true);
		thread.start();
		TimeUnit.SECONDS.sleep(2);

	}

}
