package three;
import java.util.*;
public class Generotor {
	private Random random = new Random(22);
	public Instrument next(){
		switch (random.nextInt(5)) {
		case 0:
			return new Wind();
		case 1:
			return new Percussion();
		case 2:
			return new Stringed();
		case 3:
			return new Brass();
		case 4:
			return new Woodwind();
		default:
			return new Instrument();
		}
	}

}
