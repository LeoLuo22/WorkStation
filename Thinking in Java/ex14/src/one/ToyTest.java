package one;

import static com.leoluo.util.Print.*;

interface HasBatteries{}
interface Waterproof {}
interface Shoots {}

class Toy{
	//Toy() {}
	Toy(int i) {}
}

class FancyToy extends Toy implements HasBatteries, Waterproof, Shoots{
	FancyToy() { super(1); }
}
public class ToyTest {
	static void printInfo(Class cc){
		print("Class name: " + cc.getName() + " is interface?" + cc.isInterface());
		print("Simple name: " + cc.getSimpleName());
		print("Canonical name: " + cc.getCanonicalName());
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Class c = null;
		try{
			c = Class.forName("one.FancyToy");
		}catch (ClassNotFoundException e) {
			// TODO: handle exception
			print("Can't find fancytoy");
			System.exit(1);
		}
		printInfo(c);
		for(Class face : c.getInterfaces())
			printInfo(face);
		Class up = c.getSuperclass();
		Object object = null;
		try{
			object = up.newInstance();
		}catch (InstantiationException e) {
			print("Can't in");
			System.exit(1);
			// TODO: handle exception
		}catch (IllegalAccessException e) {
			// TODO: handle exception
			print("Can");
			System.exit(1);
		}
		printInfo(object.getClass());

	}

}
