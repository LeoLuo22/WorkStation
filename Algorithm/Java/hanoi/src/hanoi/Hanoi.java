package hanoi;
import java.util.Scanner;
import java.text.MessageFormat;

public class Hanoi {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter the value of hanoi: ");
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		hanoi('A', 'B', 'C', n);
		

	}
	static void hanoi(char A, char B, char C, int n){
		if(n == 1){
			System.out.println(MessageFormat.format("Move dish {0} from {1} to {2}", n, A, C));
		}
		else{
			hanoi(A, C, B, n - 1);
			System.out.println(MessageFormat.format("Move dish {0} from {1} to {2}", n, A, C));
			hanoi(B, A, C, n - 1);
		}
	}
}
