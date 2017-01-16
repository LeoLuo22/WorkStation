package demos;

/**
 * Created by Leo on 2017/1/14.
 */
public class Throttle {
    /**
     * Throttle object simulate the throttle that controls fuel's flow.
     */
    private int top;
    private int position;

    public Throttle (){
        /**
         * Construct function without arguments
         */
        this.top = 1;
        this.position = 0;
    }

    public Throttle(int size){
        /**
         * 构造处于指定位置的油门
         * @param size
         *  size of a throttle
         * @precondition
         *  size > 0
         * @postcondition
         *  使用关闭点之上的指定刻度初始化该油门，并且当前它是关闭的
         * @throws IllegalArgumentException
         *  size is negative
         */
        if (size <=0) throw new IllegalArgumentException("size <= 0:" + size);
        this.top =size;
    }

    public Throttle (int top, int position){
        /**
         * Construct function
         * @param top
         *  size of throttle
         * @param position
         *  initial position
         * @throws IllegalArgumentException
         *  top is negative or position is negative
         */
        if (top <= 0 || position < 0) throw new IllegalArgumentException("Can't be negetive. ");
        this.top = top;
        this.position = position;
    }

    public double getFlow(){
        /**
         * Get current flow of throttle
         * @return
         *  Current flow / max flow. Values ranges in [0.0, 1.0]
         */
        return (double) this.position / (double) this.top;
    }

    public boolean isOn(){
        /**
         * Check whether the throttle is on
         * @return
         *  if position > 0 then true
         */
        return (this.position > 0);
    }

    public void shutOff(){
        /**
         * Shut off throttle
         * @postcondition
         *  Flow of throttle is off
         */
        this.position = 0;
    }

    public void shift (int amount){
        /**
         * Up or down throttle's position
         * @param amount
         *  size of up or down(positive->up, negative->down)
         * @postcondition
         *  position of throttle moved as the given value. If result exceed
         *  top position, stayed in top position, so as the min position.
         */
        if (amount > this.top - this.position)
            this.position = this.top;
        else if (this.position + amount < 0)
            this.position = 0;
        else
            this.position += amount;
    }

    public boolean isBiggerthanHalfMax (){
        /**
         * @return
         *  if current flow bigger than half of the max flow, return true.
         */
        return (this.getFlow() > 0.5);
    }
}
