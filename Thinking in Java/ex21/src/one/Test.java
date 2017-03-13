package one;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Test implements Runnable{
	public void run(){
		for(int i = 0; i < 3; ++i){
			System.out.print("µÚ" + i + "´Î");
			Thread.yield();
		}
		return;
	}
	public Test(){
		System.out.print("Start");
		System.out.print("End");
	}
	public static void main(String[] args) {
		// TODO Auto-generated method s
			ExecutorService executorService  = Executors.newSingleThreadExecutor();
			for(int i = 0; i < 5; ++i){
				executorService.execute(new Test());
			}
			executorService.shutdown();

	}

}
