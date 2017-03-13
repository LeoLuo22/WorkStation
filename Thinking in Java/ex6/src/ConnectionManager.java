import javax.imageio.event.IIOReadWarningListener;
import javax.xml.bind.ValidationEvent;

class Connection {
	private Connection(){}
	public static Connection makeConnect(){
		return new Connection();
	}

}

public class ConnectionManager{
	private static Connection[] con;
	public static Connection make(){
		return Connection.makeConnect();
	}
	public static void main(String args[]){
		Connection t = ConnectionManager.make();
		for(int i = 0; i < 10; ++i)
			con[i] = Connection.makeConnect();
	
}


}