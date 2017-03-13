package one;

public class LiftOff implements Runnable{
	protected int countDown = 10;
	private static int taskCount = 0;
	private final int id = taskCount++;
	public LiftOff() {}
	public LiftOff(int countDown){
		this.countDown = countDown;
	}
	public String status(){
		return "#" + id + "(" + (countDown > 0 ? countDown : "LiftOff!") + "), ";
	}
	public void run(){
		while(countDown-- > 0){
			System.out.print(status());
			Thread.yield();
		}
	}
	public static void main(String[] args){
		Thread thread = new Thread(new LiftOff());
		thread.start();
		new Thread(new LiftOff()).start();
		new Thread(new LiftOff()).start();
		System.out.println("Hello");
	}

}
