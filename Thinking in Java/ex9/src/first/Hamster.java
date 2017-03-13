package first;

import com.leoluo.util.Print;

public class Hamster extends Rodent{
	public static void  eat(Rodent r){
		Print.print("Haha");
	}
	public static void main(String[] args){
		Rodent rodent = new Hamster();
		eat(rodent);
	}

}
