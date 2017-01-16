package com.leo.solutions;

/**
 * Created by Leo on 2017/1/16.
 */
public class Statistician {
    private int length = 0;//序列的长度
    private double min;//序列的最小值
    private double max;//序列的最大值
    private double sum = 0;//序列的和
    private double current;

    public void nextNumber (double value){
        /**
         * assigned value to Statistics value
         * @param value
         *  new value add to the queue
         */
        this.length += 1;
        this.sum += value;
        if (this.min > value)
            this.min = value;
        if (this.max < value)
            this.max = value;
        this.current = value;
    }

    public static double getAverage (Statistician statistician){
        /**
         * Get the average value of a queue
         * @param statistician
         *  given queue
         * @return
         *  average value
         */
        if (statistician.length == 0)
            return Double.NaN;
        return  statistician.sum / statistician.length;
    }

    public int getLength (){
        /**
         * Get queue's length
         * @return
         *  queue's length
         */
        return this.length;
    }

    public double getCurrent (){
        /**
         * Get the last value
         * @return
         *  current value
         */
        if (this.length == 0)
            return Double.NaN;
        return this.current;
    }

    public double getSum (){
        /**
         * Get sum
         * @return
         *  sum
         */
        return this.sum;
    }

    public double getMin (){
        /**
         * Get the minium
         * @return
         *  minium
         */
        if (this.length == 0)
            return Double.NaN;
        return this.min;
    }

    public double getMax(){
        /**
         * Get the max value
         * @return
         *  max value
         */
        if (this.length == 0)
            return Double.NaN;
        return this.max;
    }

    public static Statistician addTwo(Statistician s1, Statistician s2){
        /**
         * Add two statistician
         * @param s1
         *  first
         * @param s2
         *  second
         * @return
         *  if s1 and s2 are different, return a new statistician,
         *
         */
        if (s1 == null || s2 == null)
            throw new IllegalArgumentException("Statistician can't be null. ");
        if (s1 == s2)
            throw new IllegalArgumentException("The two can't be the same. ");

        Statistician result = new Statistician();
        result.min = s1.min + s2.min;
        result.max = s1.max + s2.max;
        result.current = s1.current + s2.current;
        result.length = s1.length + s2.length;

        return result;
    }

    public static void main(String[] args){
        Statistician statistician = new Statistician();
        statistician.nextNumber(1.1);
        statistician.nextNumber(-2.4);
        statistician.nextNumber(0.8);
        System.out.println(statistician.getMax());
        System.out.println(statistician.getMin());
        System.out.println(statistician.getCurrent());
        System.out.println(statistician.getSum());
        System.out.println(Statistician.getAverage(statistician));
    }
}
