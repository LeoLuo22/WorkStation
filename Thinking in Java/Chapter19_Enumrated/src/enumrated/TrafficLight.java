package enumrated;

import static com.leoluo.util.Print.*;
//静态导入枚举类型
import static enumrated.Signal.*;

public class TrafficLight {
	Signal color = RED;//静态导入，无需enum修饰
	
	//小型状态机
	public void change(){
		switch (color) {
		case RED:
			color = GREEN;		
			break;
			
		case GREEN:
			color = YELLOW;
			break;

		case YELLOW:
			color = RED;
			break;
		}
	}
	
	public String toString(){
		return "The traffic light is: " + color;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TrafficLight trafficLight = new TrafficLight();
		for(int i = 0; i < 7; ++i){
			print(trafficLight);
			trafficLight.change();
		}

	}

}
