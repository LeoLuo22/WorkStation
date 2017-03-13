package three;
import two.*;

public class Tiger {
	protected class MaleTiger implements Animal{
		public MaleTiger() {
			// TODO Auto-generated constructor stub
		}

		public void eat(){
			System.out.println("MaleTiger");
		}
		private int i;
	}
	public static void main(String[] args){
		Tiger tiger = new Tiger();
		//tiger.i = 5;
	}

}
