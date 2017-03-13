package three;

import java.util.Random;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class Test implements Runnable{
	public void run(){
		Random random = new Random(22);
		int sleepTime = random.nextInt(10) + 1;
		try {
			TimeUnit.SECONDS.sleep(sleepTime);
			System.out.println("I slept " + sleepTime + (sleepTime > 1 ? " seconds" : " second"));
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ExecutorService executorService = Executors.newCachedThreadPool();
		for(int i = 0; i < 10; ++i){
			executorService.execute(new Test());
		}
		executorService.shutdown();

	}

}
