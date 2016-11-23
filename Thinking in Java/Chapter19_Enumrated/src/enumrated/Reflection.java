package enumrated;

import java.lang.reflect.Method;
import java.lang.reflect.Type;
import java.util.Set;
import java.util.TreeSet;

import static com.leoluo.util.Print.*;


enum Explore {
	HERE, THERE
}

public class Reflection {
	public static Set<String> analyze(Class<?> enumClass) {
		print("-----Analyzing " + enumClass + "-----");
		print("Interfaces");
		for (Type type : enumClass.getGenericInterfaces())
			print(type);
		print("Base: " + enumClass.getSuperclass());
		print("Methods ");
		Set<String> methods = new TreeSet<String>();
		for (Method method : enumClass.getMethods())
			methods.add(method.getName());
		print(methods);
		return methods;

	}

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Set<String> exploreMethods = analyze(Explore.class);
		Set<String> enumMethods = analyze(Enum.class);
		print("Explore.containsAll(Enum)? " + exploreMethods.containsAll(enumMethods));
		printnb("Explore.removeAll(Enum): ");
		exploreMethods.removeAll(enumMethods);
		print(exploreMethods);
	}

}
