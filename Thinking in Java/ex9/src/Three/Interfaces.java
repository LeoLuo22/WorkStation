package Three;

interface Canfly{
	void fly();
}
interface CanFlyAndJump extends Canfly{
	void jump();
}
interface CanFlyAndSwim extends Canfly{
	void swim();
}
class Init implements Canfly, CanFlyAndJump, CanFlyAndSwim{
	public void jump(){
		System.out.println("Jump");
	}
	public void fly(){
		System.out.println("Fly");
	}
	public void swim(){
		System.out.println("Swim");
	}
}
public class Interfaces {
	public static void a(CanFlyAndJump a){
		a.jump();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Init init = new Init();
		a(init);
		

	}

}
