package two;
import static com.leoluo.util.Print.*;

public class Circle extends Shape{
	@Override
	public void draw(){print("Circle.draw()");}
	@Override
	public void erase(){print("Circle.erase()");}
	@Override
	public void new_method(){
		print("Circle's new method");
	}
}

