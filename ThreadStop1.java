class StopThread extends Thread{
	public boolean stop;
	
	public void run() {
		while (!stop) {
			System.out.println("������...");
			try {
				Thread.sleep(1);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		System.out.println("���� ����");
	}
	
}

public class ThreadStop1 {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StopThread t = new StopThread();
		t.start();
		
		try {
			Thread.sleep(3);
		} catch (Exception e) {
			// TODO: handle exception
		}
		
		t.stop = true;
		
		
	}

}
