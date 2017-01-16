package com.leo.solutions;

/**
 * Created by Leo on 2017/1/16.
 */
public class Lock {
    private short x;
    private short y;
    private short z;
    private boolean isClockwise = true;

    public Lock (short x, short y, short z){
        /**
         * initialize x, y ,z, the three numbers
         * of combination.
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

    public void setXYZ(short x, short y, short z){
        /**
         * change combination
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

    public void rotate (boolean isClockwise, short value){
        if (isClockwise)
            System.out.println("当前锁正在顺时针旋转");
        else
            System.out.println("当前锁正在逆时针旋转");
        this.isClockwise = !this.isClockwise;
    }
}
