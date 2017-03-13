package one;

public class Outer {
	class Inner{
		private int i;
		public Inner(int j) {
			// TODO Auto-generated constructor stub
			i = j;
		}
		public int read(){
			return i;
		}
	}
	public Inner newInner(int i){
		return new Inner(i);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Outer outer = new Outer();
		Outer.Inner inner = outer.newInner(5);
		System.out.println(inner.read());

	}

}

class Test{
	Outer outer = new Outer();
	Outer.Inner inner = outer.new Inner(9);
}