package one;

import java.util.ArrayList;
import java.util.List;

public class InfiniteRecursion {
	/*
	public String toString(){
		return "Infinite" + Object.toString() + "\n";
	}
	*/

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<InfiniteRecursion> v = new ArrayList<InfiniteRecursion>();
		for(int i = 0; i < 10; ++i){
			v.add(new InfiniteRecursion());
		}
		System.out.println(v.toString());
		String string = "HEllo";
		String string2 = new String("HEllo");
		System.out.println(string.equals(string2));
		String s = string.substring(0, 1);
		System.out.println(s);
	}

}
