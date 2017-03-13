class Component1{
	Component1(){
		System.out.println("Component1 constructor");
	}
}
class Component2{
	Component2(){
		System.out.println("Component2 constructor");
	}
}
class Component3{
	Component3(){
		System.out.println("Component3 constructor");
	}
}

public class Root {
	Root(){
		System.out.println("Root constructor");
	}
	public Component1 component1 = new Component1();
	public Component2 component2 = new Component2();
	public Component3 component3 = new Component3();
	public static void main(String[] args) {
		Stem s = new Stem();
	}
	

}
class Stem extends Root{
	Stem() {
		// TODO Auto-generated constructor stub
		System.out.println("Stem constructor");
	}
}
