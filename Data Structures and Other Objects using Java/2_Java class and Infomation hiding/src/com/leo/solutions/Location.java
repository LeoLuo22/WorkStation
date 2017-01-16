package com.leo.solutions;

/**
 * Created by Leo on 2017/1/16.
 */
public class Location {
    private double x;
    private double y;
    private double z;

    public Location(double x, double y, double z){
        /**
         * Make location to a given point.
         * @param x
         *  x
         * @param y
         *  y
         * @param z
         *  z
         */
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public void move(char axis, double value){
        /**
         * move location to somewhere alone a axis.
         * @param axis
         *  axis that move to
         * @param value
         *  the distance location moved
         */
        switch (axis){
            case 'x':
            case 'X':
                this.x += value;
                break;
            case 'y':
            case 'Y':
                this.y = y;
                break;
            case 'z':
            case 'Z':
                this.z = z;
                break;
        }
    }

    @Override
    public String toString(){
        return "(" + this.x + ", " + this. y + ", " + this.z + ")";
    }

    public void rotate(char axis, double theta){
        /**
         * rotate the location
         * @param axis
         *  the axis rotate
         * @param theta
         *  the angle
         */
        double a = this.x;
        double b = this.y;
        double c = this.z;

        switch (axis){
            case 'x':
            case 'X':
                this.x = a;
                this.y = b * Math.cos(theta) - c * Math.sin(theta);
                this.z = b * Math.sin(theta) + c * Math.cos(theta);
                break;
            case 'y':
            case 'Y':
                this.x = a * Math.cos(theta) + c * Math.sin(theta);
                this.y = b;
                this.z = -a * Math.sin(theta) + c * Math.cos(theta);
                break;
            case 'z':
            case 'Z':
                this.x = a * Math.cos(theta) - b * Math.sin(theta);
                this.y = a * Math.sin(theta) + b * Math.cos(theta);
                this.z = c;
                break;
        }
    }

    public static void main(String args[]){
        Location location = new Location(1.0,2.0, 3.0);
        System.out.println(location);
        location.rotate('x', 90.0);
        System.out.println(location);
    }
}
