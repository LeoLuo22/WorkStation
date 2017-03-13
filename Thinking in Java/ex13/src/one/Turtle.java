package one;

import java.io.PrintStream;
import java.util.Formatter;

public class Turtle {
	private String name;
	private Formatter formatter;
	public Turtle(String name, Formatter formatter){
		this.name = name;
		this.formatter = formatter;
	}
	public void move(int x, int y){
		formatter.format("%s The Turtlr is at (%d, %d)\n", name, x, y);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		PrintStream outAlias = System.out;
		Turtle tommy = new Turtle("Tommy", new Formatter(System.out));
		Turtle terry = new Turtle("Terry", new Formatter(outAlias));
		Turtle david = new Turtle("David", new Formatter(System.err));
		tommy.move(0, 0);
		terry.move(1, 2);
		david.move(2, 4);

	}

}
