package one;
import java.util.*;
import static com.leoluo.util.Print.*;

import java.util.ArrayList;

public class Gerbil {
	private int getbilNumber;
	public Gerbil(int i){
		this.getbilNumber = i;
	}
	public void hop(){
		print("Gerbil" + this.getbilNumber + "hops");
	}
	public String toString(){
		return "Hello";
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Gerbil> gerbils = new ArrayList<Gerbil>();
		for(int i = 0; i < 10; ++i){
			gerbils.add(new Gerbil(i));
		}
		Iterator<Gerbil> iterator = gerbils.iterator();
		read(iterator);

	}
	public static void read(Iterator it){
		while(it.hasNext())
			print(it.next());
	}

}

class Demo{
	public int i;
	private String string = "Hello";
	public String toString(){
		return this.string;
	}
}
