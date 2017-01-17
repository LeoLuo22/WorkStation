package com.leo.geometry;

/**
 * Created by Leo on 2017/1/15.
 */
public class Location implements Cloneable{
    /**
     * Location object traces 2D's location.
     */
    private double x;
    private double y;

    public Location (double xInitial, double yInitial){
        /**
         * Construct a location with the given coordinate
         * @param xInitial
         *  initial x coordinate of location
         * @param yInitial
         *  initial y coordinate of location
         * @postcondition
         *  Using the given coordinate to initialize location
         */
        this.x = xInitial;
        this.y = yInitial;
    }

    public double getX (){
        /**
         * @return
         *  location's x value
         */
        return this.x;
    }

    public double getY (){
        /**
         * @return
         *  location's y value
         */
        return this.y;
    }

    public Object clone (){
        /**
         * Generate a copy of the location
         * @return
         *  copy of the location. warning:
         *  must cast it before use it.
         */
        Location answer;
        try {
            answer = (Location) super.clone();
        }
        catch (CloneNotSupportedException e){
            throw new RuntimeException("This class does not implement Cloneable");
        }

        return answer;
    }

    public static double distance (Location p1, Location p2){
        /**
         * calculate the distance between p1 and p2
         * @param p1
         *  first point
         * @param p2
         *  second point
         * @return
         *  distance between p1 and p2
         * @warning
         *  if the result is overflow, then the answer will be Double.POSITIVE_INFINITY.
         *  if one of the location is null, the anwser will be Double.NaN.
         */
        double a, b, c_squared;
        if ((p1 == null) || (p2 == null))
            return Double.NaN;

        //calculate the distance between two points
        a = p1.x - p2.x;
        b = p1.y - p2.y;
        c_squared = a * a + b * b;

        return Math.sqrt(c_squared);
    }

    public static Location midpoint (Location p1, Location p2){
        /**
         * Generate and return the midpoint of two points
         * @param p1
         *  first location
         * @param p2
         *  second location
         * @return
         *  midpoint of p1 and p2
         * @warning
         *  if p1 or p2 is null, return null
         */
        if ((p1 == null) || (p2 == null))
            return null;

        return new Location((p1.x + p2.x) / 2, (p2.y + p1.y) / 2);
    }

    public void rotate90 (){
        /**
         * Ratate 90 degree of origin
         * @postcondition
         *  location rotated
         */
        double xNew;
        double yNew;

        xNew = this.y;
        yNew = this.x;

        this.x = xNew;
        this.y = yNew;
    }

    public void shift (double xAmount, double yAmount){
        /**
         * move location by the given value
         * @param xAmount
         *  x value
         * @param yAmount
         *  y value
         */
        this.x += xAmount;
        this.y += yAmount;
    }

    public String toString (){
        /**
         * @return
         *  string that show the location
         */
        return ("(" + this.x + "," + this.y + ")");
    }

    public boolean equals (Object obj){
        /**
         * compare this location with other
         * @param obj
         *  the other location
         * @return
         *  if the value is equal, return true
         */
        if (obj instanceof Location){
            Location candidate = (Location) obj;
            return ( candidate.x == this.x) && (candidate.y == this.y);
        }
        else {
            return false;
        }
    }

    public static void main(String[] args){
        Location origin = new Location(0,0);
        Location p = new Location(1,1);
        System.out.println(Location.distance(origin, p));
        Location p1 = Location.midpoint(origin, p);
        System.out.println(p1);
    }
}
