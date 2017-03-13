package four;
import three.*;
import two.*;

public class LittleTiger extends Tiger{
	public Animal create(){
		Tiger tiger = new Tiger();
		Tiger.MaleTiger maleTiger = tiger.new MaleTiger();
		return maleTiger;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
