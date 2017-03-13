package ex5;
import static com.leoluo.util.Print.*;
import static com.leoluo.util.Range.*;

public class Test {

	public static void main(String[] args) {
		print("Hello");
		int[] n = range(5);
		print(n[4]);
		

	}
	//static Table table = new Table();
	//static Cupboard cupboard = new Cupboard();

}

class Bowl{
	Bowl(int maker){
		System.out.println("Bowl" + maker);
	}
	void f1(int maker){
		System.out.println("f1");
	}
}

class Table{
	static Bowl bowl1 = new Bowl(1);
	Table(){
		System.out.println("Table");
		bowl2.f1(1);
	}
	void f2(int maker){
		System.out.println("f2");
	}
	static Bowl bowl2 = new Bowl(2);
}
class Cupboard{
	Bowl bowl3 = new Bowl(3);
	static Bowl bowl4 = new Bowl(4);
	Cupboard(){
		System.out.println("Cupboard");
		bowl4.f1(2);
	}
	void f3(int maker){
		System.out.println("f3");
	}
	static Bowl bowl5 = new Bowl(5);
}