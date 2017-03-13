package four;

import com.leoluo.util.Stack;
import static com.leoluo.util.Print.*;

public class MyStack {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack<Character> stack = new Stack<Character>();
		String string = "+U+n+c---+e+r+t---+a-+i-+n+t+y---+-+r+u--+l+e+s---";
		for(int i=0; i< string.length(); ++i){
			if(string.charAt(i) == '+'){
				stack.push(string.charAt(i+1));
			}
			if(string.charAt(i) == '-'){
				print(stack.pop());
			}
		}

	}

}
