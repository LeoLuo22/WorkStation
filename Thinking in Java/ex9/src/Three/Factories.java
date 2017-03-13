package Three;

import static com.leoluo.util.Print.*;

interface Service{
	void method1();
	void method2();
}
interface ServiceFactory{
	Service getService();
}

class Implementation1 implements Service{
	Implementation1() {}
	public void method1(){
		print("Implementation1 method1");
	}
	public void method2(){
		print("Implementation1 method2");
	}
}

class Implementation2 implements Service{
	Implementation2(){}
	public void method1(){
		print("Implementation2 method1");
	}
	public void method2(){
		print("Implementation2 method2");
	}
	
}

class Implementation1Factory implements ServiceFactory{
	public Service getService(){
		return new Implementation1();
	}
}

class Implementation2Factory implements ServiceFactory{
	public Service getService(){
		return new Implementation2();
	}
}

public class Factories {
	
	public static void serviceConsumer(ServiceFactory fact){
		Service service = fact.getService();
		service.method1();
		service.method2();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		serviceConsumer(new Implementation1Factory());
		serviceConsumer(new Implementation2Factory());

	}

}
