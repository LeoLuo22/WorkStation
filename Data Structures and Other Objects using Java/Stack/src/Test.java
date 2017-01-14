import java.util.Stack;

/**
 * Created by Leo on 2017/1/11.
 */
public class Test {
    public static boolean isBalanced(String expression){
        final char LEFT_NORMAL = '(';
        final char RIGHT_NORMAL = ')';
        final char LEFT_CURLY = '{';
        final char RIGHT_CURLY = '}';
        final char LEFT_SQUARE = '[';
        final char RIGHT_SQUARE =']';

        Stack<Character> store = new Stack<Character>();
        int i;
        boolean failed = false;

        for(i = 0; !failed && (i < expression.length()); i++){
            switch (expression.charAt(i)){
                case LEFT_NORMAL:
                case LEFT_CURLY:
                case LEFT_SQUARE:
                    store.push(expression.charAt(i));
                    break;
                case RIGHT_NORMAL:
                    if (store.isEmpty() || (store.pop() != LEFT_NORMAL))
                        failed = true;
                    break;
                case RIGHT_CURLY:
                    if (store.isEmpty() || (store.pop() != LEFT_CURLY))
                        failed = true;
                    break;
                case  RIGHT_SQUARE:
                    if (store.isEmpty() || (store.pop() != LEFT_SQUARE))
                        failed = true;
                    break;
            }
        }
        return (store.isEmpty() && !failed);
    }

    public static void main(String[] args){
        System.out.println(isBalanced("(){hello}"));
    }
}
