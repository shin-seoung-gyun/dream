
public class ThreadInterrupt2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Runnable task = () ->{
			while(!Thread.currentThread().isInterrupted()) {
				System.out.println("���� ��...");
			}
			System.out.println("���� ����");
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
