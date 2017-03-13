package com.ex;
import java.util.*;

import static com.leoluo.util.Print.*;

public class Test {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		Random rand = new Random();
		int fcount =0, tcount = 0;
		for(int j = 0; j <= 99; ++j){
			if(rand.nextBoolean()){
				tcount += 1;
			}
			else
				fcount += 1;
				
		}
		print("hello");
		System.out.println("True:" + tcount + "Flase:" + fcount);
		double rate = tcount / fcount;
		System.out.println("Rate: " + rate);


	}
	

}
