package com.leo.solutions;

/**
 * Created by Leo on 2017/1/16.
 */
public class Quadratic {
    /**
     * ax^2 + bx + c
     */
    private double a;
    private double b;
    private double c;

    public Quadratic(){
        this.a = 0.0;
        this.b = 0.0;
        this.c = 0.0;
    }

    public Quadratic(double a, double b, double c){
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public void setQuadratic(double a, double b, double c){
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double getA(){
        return this.a;
    }

    public double getB(){
        return this.b;
    }

    public double getC(){
        return this.c;
    }

    public double calculate(double x){
        return this.a * x * x + this.b * x + this.c;
    }

    public static Quadratic sum(Quadratic q1, Quadratic q2){
        return new Quadratic(q1.a + q2.a, q1.b + q2.b, q1.c + q2.c);
    }

    public static Quadratic scale(double r, Quadratic q){
        return new Quadratic(r * q.a, r * q.b, r * q.c);
    }

    private int numofRoot(){
        /**
         * return the number of root of quadratic
         * @return
         *  number of roots
         */
        double delta = this.b * this.b - 4 * this.a * this.c;
        if (this.a == 0 && this.b == 0 && this.c == 0) //if all the coefficient is zero, then every x is a root
            return 3;
        if ((this.a == 0 && this.b == 0 && this.c != 0) || (this.a != 0 && delta < 0))
            return 0;
        if ((this.a == 0 && this.b != 0) || (this.a != 0 && delta == 0))
            return 1;
        return 2;
    }

    public double[] getRoot(){
        /**
         * Get the root of quadratic
         * @return
         *  results
         */
        if (this.numofRoot() <= 0)
            throw new RuntimeException("Quadratic at least need one root");

        if (this.numofRoot() == 2){
            double[] results = new double[2];
            double delta = this.b * this.b - 4 * this.a * this.c;
            results[0] = (-this.b - Math.sqrt(delta)) / (2 * a);
            results[1] = (-this.b + Math.sqrt(delta)) / (2 * a);
            return results;
        }

        double[] results = new double[1];

        if (this.a == 0){
            results[0] = (-this.c) / this.b;
            return results;
        }

        results[0] = (-this.b) / (2 * this.a);
        return results;
    }

    @Override
    public String toString(){
        return this.a + "x^2" + "+" + this.b + "x" + "+" + this.c;
    }

    public static void main(String[] args){
        Quadratic quadratic = new Quadratic(2.0, 8.0, 6.0);
        System.out.println(quadratic.getRoot()[0]);
    }
}
