import static com.leoluo.util.Print.*;

class Game{
	Game(int i){
		//print("Game cons" + i);
	}
}
class BoardGame extends Game{
	BoardGame(int i){
		super(i);
		print("Board cons" + i);
	}
}
public class Chess extends BoardGame{
	Chess(int i){
		super(i);
		//print("Chess Cons" + i);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Chess x = new Chess(1);

	}

}
