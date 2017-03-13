package one;
import static com.leoluo.util.Print.*;

public class Cycle {
	public static void ride(Cycle c){
		print("Cycle wheels are: " + c.wheels());
		print("Hello");
	}
	public int wheels(){
		return 0;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Cycle[] cycles = {
				new Unicycle(),
				new Bicycle(),
				new Tricycle()
		};
		((Unicycle)cycles[0]).balance();
		((Bicycle)cycles[1]).balance();
		//cycles[2].balance;

	}

}

class Unicycle extends Cycle{
	@Override
	public int wheels(){
		return 1;
	}
	public void balance(){
		print("Uni balance");
	}
	
}

class Bicycle extends Cycle{
	public void balance(){
		print("Cycle balace");
	}
	
}

class Tricycle extends Cycle{
	
}