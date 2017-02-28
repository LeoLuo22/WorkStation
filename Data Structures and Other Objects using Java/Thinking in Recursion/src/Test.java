/**
 * Created by Leo on 2017/2/27.
 */
public class Test {
    public static void writeVertical(int number){
        /**
         * 纵向打印一个非负整数
         * @param number
         *  要打印的数字
         * @precondition
         *  number >= 0
         * @postcondition
         *  number的所有位被纵向打印出来
         */
        if (number < 10)
            System.out.println(number);
        else {
            writeVertical(number / 10);
            System.out.println(number % 10);
        }
    }

    public static void superWriteVertical(int number){
        /**
         * 纵向打印一个整数
         * @param number
         *  要打印的数字
         * @postcondition
         *  number所有位纵向打出。如果number是负数，最顶上的一行是一个负号。
         */
        if (number < 0){
            //number = Math.abs(number);
            System.out.println("-");
            superWriteVertical(-number);
        }

        if (number < 10){
            System.out.println(number);
        }
        else {
            superWriteVertical(number / 10);
            System.out.println(number % 10);
        }
    }

    /*
    public static void f1(int n){
        System.out.println(n);
        if (n > 1)
            f1(n-1);
    }

    public static void f2(int n){
        if (n > 1)
            f2(n-1);
        System.out.println(n);
    }
    */
    public static void f3 (int n) {
        System.out.println(n);
        if (n > 1)
            f3(n-1);
        System.out.println(n);
    }

    public static void cheers (int n) {
        if (n <= 1)
            System.out.println("Hurrah");
        else {
            System.out.println("Hip");
            cheers(n-1);
        }
    }

    public static void symbol(int n) {
        /**
         * 打印指定参数的星号和感叹号
         * @param n
         *  非负整数
         * @precondition
         *  n为非负整数
         */
        System.out.print("*");
        if (n > 1)
            symbol(n-1);
        System.out.print("!");
    }

    public static void main(String[] args){
        //superWriteVertical(12345);//writeVertical(1234);
        //cheers(3);
        symbol(3);
    }
}
