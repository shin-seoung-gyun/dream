
public class ThreadMain3 {

	public static void main(String[] args) {//스레드 클래스를 상속받은 클래스를 만들어서 따로 runable인터페이스를 사용하지 않고 바로 사용.
		// TODO Auto-generated method stub
		Thread th = new SubThread();
		th.start();
		for(int i = 0; i < 5; i++) {
			System.out.println("안녕.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		

	}

}

class SubThread extends Thread {
	public void run() {
		for(int i = 0; i < 5; i++) {
			System.out.println("잘가.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
	}
}