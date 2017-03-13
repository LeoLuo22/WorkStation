package three;
import static com.leoluo.util.Print.*;

import java.awt.event.MouseWheelEvent;
import java.util.*;

import org.omg.CORBA.PRIVATE_MEMBER;


class Instrument{
	void play(Note n){
		print("Instrument.play" + n);
	}
	public String toString(){
		return "Instrument";
	}
	void adjust(){
		print("Adjusting instrument");
	}
}
class Wind extends Instrument{
	@Override
	void play(Note n){
		print("Wind.play" + n);
	}
	@Override
	public
	String toString(){
		return "Wind";
	}
	@Override
	void adjust(){
		print("Adjusting wind");
	}
}
class Percussion extends Instrument{
	void play(Note n){
		print("Percussion.play" + n);
	}
	public String toString(){
		return "Percussion";
	}
	void adjust(){
		print("Adjusting percussion");
	}
}
class Stringed extends Instrument{
	void play(Note n){
		print("Stringed.play" + n);
	}
	public String toString(){
		return "Stringed";
	}
	void adjust(){
		print("Adjusting Stringed");
	}
}
class Brass extends Wind{
	void play(Note n){
		print("Brass.play" + n);
	}
	void adjust(){
		print("Adjusting brass");
	}
}
class Woodwind extends Wind{
	void play(Note n){
		print("Woodwind.play" + n);
	}
	public String toString(){
		return "Woodwind";
	}
}
public class Music3 {
	public static void tune(Instrument i){
		i.play(Note.MIDDLE_C);
	}
	public static void tuneAll(Instrument[] e){
		for(Instrument instrument : e)
			tune(instrument);
	}
	private static Generotor generotor = new Generotor();

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Instrument[] instruments = new Instrument[10];
		for(int i = 0; i < instruments.length; i++)
			instruments[i] = generotor.next();
		tuneAll(instruments);
		Instrument instrument =  new Woodwind();
		print(instrument);
	}

}
