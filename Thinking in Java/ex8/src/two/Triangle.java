package two;
import static com.leoluo.util.Print.*;

public class Triangle extends Shape{
	@Override
	public void draw() {
		print("Triangle.draw()");
	}
	@Override
	public void erase() {
		print("Tringle.erase()");
	}

}
