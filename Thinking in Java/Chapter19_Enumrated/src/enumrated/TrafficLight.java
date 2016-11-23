package enumrated;

import static com.leoluo.util.Print.*;
//��̬����ö������
import static enumrated.Signal.*;

public class TrafficLight {
	Signal color = RED;//��̬���룬����enum����
	
	//С��״̬��
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
