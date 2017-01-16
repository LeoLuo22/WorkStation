package demos;

/**
 * Created by Leo on 2017/1/15.
 */
public class Clock {
    private int hour;
    private int minute;
    final private int MAX_MINUTE = 60;

    public Clock (){
        /**
         * Construc function without arguments.
         * Initail time to midnight.
         */
        this.hour = 0;
        this.minute = 0;
    }

    public Clock (int hour, int minute){
        /**
         * Construct function
         * @param hour
         *  hour of time
         * @param minute
         *  minute of time
         * @throws IllegalArgumentException
         *  hour should between 0 to 23
         *  minute should between 0 to 59
         */
        if (!(hour >= 0 && hour <=23)) throw new IllegalArgumentException("hour should between 0 to 23");
        if (!(minute >=0 && minute <=59)) throw new IllegalArgumentException("minute should between 0 to 59");
        this.hour = hour;
        this.minute = minute;
    }

    public boolean getTime(){
        /**
         * @return
         *  if current time is before noon, return true.
         */
        if (this.hour <= 11)
            return true;
        else if (this.hour == 12 && this.minute == 0)
            return true;
        return false;
    }

    public void setMinute (int minute){
        /**
         * Set time ahead of given minute;
         * @param minute
         *  if minute is positive, than ahead of time.
         * @throws IllegalArgumentException
         *  minute should between at 0 to 59
         */
        if (!(minute >=0 && minute <=59)) throw new IllegalArgumentException("minute should between 0 to 59");

        if (this.minute - minute < 0){
            this.minute = MAX_MINUTE - (minute - this.minute);
            this.hour -= 1;
        }

        else if (this.minute - minute >= 60){
            this.minute = MAX_MINUTE - (this.minute - minute);
            this.hour += 1;
        }

        else
            this.minute -= minute;
    }
}
