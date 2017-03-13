package ex5;
import com.leoluo.util.Print.*;

public class Bucks {

		String s = "Hello";
		Bucks(int i, String s){
			this(s);
			System.out.println("int");
		}
		Bucks(String s){
			System.out.println("String");
		}
		void foo1(){
			foo2();
			this.foo2();
			System.out.println("1");
		}
		void foo2(){
			System.out.println("2");
		}

}
