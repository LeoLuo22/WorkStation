package one;

import static com.leoluo.util.Print.*;

import javax.swing.text.StyledEditorKit.ForegroundAction;

public class One {

	public static void main(String[] args) throws TestException {
		// TODO Auto-generated method stub
		//throw new TestException("HEllo");
		All all = new All();
		try {
			throw new RuntimeException(); 
		} catch (RuntimeException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}

class TestException extends Exception {
	public TestException() {
	}

	public TestException(String msg) {
		super(msg);
	}
}

class tException extends Exception {
	public tException() {
	}
}

class eException extends Exception {
}

class All {
	public static void foo() throws TestException, tException {
	}
}