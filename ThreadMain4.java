
public class ThreadMain4 {

	public static void main(String[] args) {//runable 인터페이스 사용하지않고 바로 익명 스레드 개체 안에 void run매서드를 만들어서 사용.
		// TODO Auto-generated method stub
		new Thread() {public void run(){
			for(int i = 0; i <5; i++) {
				System.out.println("잘가.");
				try {
					Thread.sleep(500);
				} catch (Exception e) {
					// TODO: handle exception
				}
			}
		}}.start();
		
		for(int i = 0; i <5; i++) {
			System.out.println("안녕.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		

	}

}
