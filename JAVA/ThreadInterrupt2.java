
public class ThreadInterrupt2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Runnable task = () ->{
			while(!Thread.currentThread().isInterrupted()) {
				System.out.println("실행 중...");
			}
			System.out.println("정상 종료");
		};
		
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
