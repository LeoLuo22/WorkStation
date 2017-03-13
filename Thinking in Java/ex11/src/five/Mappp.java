package five;
import static com.leoluo.util.Print.*;

import java.io.ObjectInputStream.GetField;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class Mappp {
	private String s;
	public Mappp(String s){
		this.s = s;
	}
	public static void Operation(Mappp s){
		print(s.s);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Last last = new Last();
		Operation(last.method());
		
	}

}

class Command{
	private Queue<Mappp> qMappps;
	public void gen(){
		this.qMappps = new LinkedList<Mappp>();
		this.qMappps.offer(new Mappp("Hello"));
		this.qMappps.offer(new Mappp("World"));
	}
	public Queue<Mappp> getele(){
		return this.qMappps;
	}
}

class Last{
	private Command command;
	public Mappp method(){
		command = new Command();
		command.gen();
		Queue<Mappp> queue = command.getele();
		return queue.poll();
		
	}
}