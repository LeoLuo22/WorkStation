package enumrated;

import static com.leoluo.util.Print.*;

public enum OzWitch {
	WEST("This is west"),
	NORTH("This is north"),
	EAST("This is east"),
	SOUTH("This is south"); //���Ҫ�����Լ��ķ�����������enumʵ�����е�������һ���ֺ�
	
	private String description;
	
	private OzWitch(String description){
		this.description = description;
	}
	
	public String getDescription(){
		return this.description;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(OzWitch witch : OzWitch.values())
			print(witch + ": " + witch.getDescription());

	}

}
