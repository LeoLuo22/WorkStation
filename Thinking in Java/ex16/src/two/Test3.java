package two;
import static com.leoluo.util.Print.*;

import java.util.Arrays;
import java.util.Random;

//import javax.swing.plaf.multi.MultiButtonUI;
public class Test3 {
	public Double[][] multi(int i, int begin, int end){
		Random random = new Random(22);
		Double[][] doubles = new Double[i][i];
		/*
		for(int j = 0; j < i; ++j){
			for(int k = 0; k < i; ++k){
				doubles[j][k] = random.nextDouble() * (end - begin) + begin;
			}
		}
		*/
		return doubles;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Test3 test3 = new Test3();
		//print(Arrays.deepToString(test3.multi(2, 2, 5)));
		int[][] a = new int[2][2];
		int[][] b = new int[2][2];
		print(Arrays.deepEquals(a, b));

	}

}
