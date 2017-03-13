package three;

import static com.leoluo.util.Print.*;

class Sleeper extends Thread{
	private int duration;
	public Sleeper(String name, int sleepTime){
		super(name);
		this.duration = sleepTime;
		this.start();
	}
	public void run(){
		try{
			sleep(duration);
		}catch (InterruptedException e) {
			// TODO: handle exception
			print(this.getName() + " was interrupted. " + " isInterrupted(): " + this.isInterrupted());
			return;
		}
		print(this.getName() + " has awakened");
	}
}

class Joiner extends Thread{
	private Sleeper sleeper;
	public Joiner(String name, Sleeper sleeper){
		super(name);
		this.sleeper = sleeper;
		this.start();
	}
	public void run(){
		try{
			sleeper.join();
		}catch (InterruptedException e) {
			// TODO: handle exception
			print("Interrupted");
		}
		print(this.getName() + " join completed");
	}
}
public class Joining {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Sleeper sleepy = new Sleeper("Sleepy", 1500);
		Sleeper grumpy = new Sleeper("grumpy", 1500);
		Joiner dopey = new Joiner("Dopey", sleepy), doc = new Joiner("Doc", grumpy);
		grumpy.interrupt();
	}

}
