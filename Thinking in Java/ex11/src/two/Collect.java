package two;

import static com.leoluo.util.Print.*;

import java.awt.event.MouseWheelEvent;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.TreeSet;

class MovieGen{
	private int i = 0;
	private String[] items;
	private int next = 0;
	public MovieGen(int size){
		items = new String[size];
	}
	public void add(String s){
		if(next < items.length);
		items[next++] = s;
	}
	public boolean end(){
		return i == items.length;
	}
	public String current(){
		return items[i];
	}
	public String next(){
		if(i <= items.length)
			i++;
		if(i == items.length)
			i = 1;
		return items[i-1];
	}
	public int length(){
		return items.length;
	}
}
public class Collect {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MovieGen movies = new MovieGen(5);
		movies.add("Forest Gump");
		movies.add("Shawshank Redempetion");
		movies.add("Hello");
		movies.add("world");
		movies.add("ÄãºÃ");
		ArrayList<String> arrayList = new ArrayList<String>();
		LinkedList<String> linkedList = new LinkedList<String>();
		HashSet<String> hashSet = new HashSet<String>();
		LinkedHashSet<String> linkedHashSet = new LinkedHashSet<String>();
		TreeSet<String> treeSet = new TreeSet<String>();
		for(int i = 0; i < movies.length(); ++i){
			arrayList.add(movies.next());
			linkedHashSet.add(movies.next());
		}
		print(arrayList);
		print(linkedHashSet);
	}

}
