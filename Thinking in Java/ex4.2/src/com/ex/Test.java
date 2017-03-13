package com.ex;
import java.util.*;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		Random rand = new Random(22);
		List big = new ArrayList();
		List small = new ArrayList();
		List equal = new ArrayList();
		for(int i = 0; i < 25; ++i){
			int j = rand.nextInt();
			int k = rand.nextInt();
			if(i < j)
				small.add(i);
			else if(i > j)
				big.add(i);
			else
				equal.add(i);
			
		}
		System.out.println(big);
		System.out.println(small);
		System.out.println(equal);
		*/
		/*
		Scanner sc = new Scanner(System.in);
		System.out.println("请输入起始位置：");
		int begin = sc.nextInt();
		System.out.println("请输入终止位置：");
		int end = sc.nextInt();
		for(int begin0 = begin; begin0 <= end; ++begin0){
			if(is_primer(begin0))
				System.out.print(begin0 + "  ");
			//System.out.println("");
		}
		
		

	}
	static boolean is_primer(int i){
		if(i == 1)
			return true;
		int count = 0;
		for(int j = 1; j <= i + 1; j++){
			if(count > 2)
				return false;
			if(i % j == 0)
				count += 1;
		}
		return true;
	}
	*/
		/*
		for(int t = 1; t <= 7; ++t){
			System.out.print(f(t));
			System.out.print(" ");
		}
	
	}
	static int f(int n){
		if(n == 1)
			return 1;
		else if(n == 2)
			return 1;
		return f(n-1) + f(n-2);
		*/
}
	

}