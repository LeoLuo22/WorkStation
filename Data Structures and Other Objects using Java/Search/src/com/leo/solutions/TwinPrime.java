package com.leo.solutions;

import java.util.Hashtable;

/**
 * Created by Leo on 2017/3/24.
 */
public class TwinPrime {
    public static boolean isPrime(int number){
        if (number == 2)
            return true;

        for(int i = 2; i < number; ++i) {
            if (number % i == 0)
                return false;
        }

        return true;
    }

    public static void main(String[] args){
        Hashtable hashtable = new Hashtable( 825);
        int[] results = new int[2];

        for(int i = 800; i < 850; ++i){
            if (isPrime(i))
                hashtable.put(i, true);
        }

        System.out.print(hashtable.entrySet());
    }
}
