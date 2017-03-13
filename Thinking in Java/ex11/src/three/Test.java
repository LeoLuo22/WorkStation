package three;
import static com.leoluo.util.Print.*;

import java.util.*;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Integer> list = new ArrayList<Integer>();
		for(int i =0; i < 10; ++i)
			list.add(i);
		List<Integer> last = new ArrayList<Integer>();
		ListIterator<Integer> it = list.listIterator(list.size());
		for(int i = 0; i < list.size(); ++i){
			if(it.hasPrevious())
				last.add(it.previous());
		}
		LinkedList<Integer> integers = new LinkedList<Integer>();
		for(int i = 0; i < 6; ++i){
			ListIterator<Integer> iterator = integers.listIterator(integers.size()/2);
			iterator.add(new Integer(i));
		}
		print(integers);

	}

}
