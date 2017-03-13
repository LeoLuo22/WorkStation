package Second;
import Second.Note;
interface Instruments {
	int VALUE = 5;
	void play(Note n);
	void adjust();
	String toString();

}
interface playable{
	
}
abstract class Wind implements Instruments, playable{
	//public v
}
