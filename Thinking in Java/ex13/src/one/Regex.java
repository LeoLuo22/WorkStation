package one;

import java.util.Arrays;

public class Regex {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String regex = "^[A-Z]\\w*.$";
		System.out.println("Asdsds1212ds.".matches(regex));
		String re = "the|you";
		System.out.println(Arrays.toString("Then, when you have found the fuck".split(re)));
		String reg = "A|E|I|O|U|a|e|i|o|u";
		System.out.println("Then, when you have found the fuck".replaceAll(reg, "_"));

	}

}
