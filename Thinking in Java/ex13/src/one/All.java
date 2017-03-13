package one;

public class All {
	public int i = 2;
	public long a = 10;
	public float f = 2.2f;
	public double d = 2.2;
	public String toString(){
		return String.format("%d", i);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		All all = new All();
		System.out.println(all);

	}

}
