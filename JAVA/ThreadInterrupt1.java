
public class ThreadInterrupt1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Runnable task = () -> {
			try {
				while(true) {
					System.out.println("실행중...");
					Thread.sleep(1);
				}
				
				
			} catch (InterruptedException e) {//인터럽트 처리코드
				// TODO: handle exception
			}
			System.out.println("정상 종료");
		};// 인터페이스를 바로 람다식으로 사용하여 세미콜론으로 닫아줘야함.
		
		Thread t = new Thread(task);
		t.start();
		
		try {
			Thread.sleep(2);
		} catch (InterruptedException e) {
			// TODO: handle exception
		}
		t.interrupt();
		
	}

}
