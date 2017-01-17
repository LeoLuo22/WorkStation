package com.leo.solutions;

/**
 * Created by Leo on 2017/1/16.
 */
public class Myrandom {
    /**
     * 线性同余产生伪随机数
     * 公式(multiplier*seed + increment) % modulus
     */
    private double seed;
    private double multiplier;
    private double increment;
    private double modulus;

    public Myrandom(double seed, double multiplier, double increment, double modulus){
        this.seed = seed;
        this.multiplier = multiplier;
        this.increment = increment;
        this.modulus = modulus;
    }

    public void setSeed(double newSeed){
        this.seed = newSeed;
    }

    public double getNext(){
        /**
         * Generate and return the next random number
         */
        this.seed = (this.multiplier * this.seed + this.increment) % this.modulus;
        return this.seed;
    }

    public double dotNext(){
        this.getNext();
        return (this.seed / this.modulus);
    }
    public static void main(String[] args){
        Myrandom myrandom = new Myrandom(1, 40, 3641, 729);
        int count = 0;
        for(int i = 0; i <= 1003; ++i){
            if (myrandom.dotNext() < 0.1)
                count += 1;
        }
        System.out.println((double) count / 1003);
    }
}
