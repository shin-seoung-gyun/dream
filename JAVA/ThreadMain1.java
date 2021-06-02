
public class ThreadMain1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Runnable() {//객체화 하지 않고 바로 익명 스레드로 만듬
			public void run() {
				for(int i = 0; i<5; i++) {
					System.out.println("잘가");
					try {
						Thread.sleep(500);
					} catch (Exception e) {
						// TODO: handle exception
					}
				}
				
			}
		}).start();//바로 start를 붙여서 실행.
		
		for(int i = 0; i<5; i++) {
			System.out.println("안녕.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		
		
		
	}

}
