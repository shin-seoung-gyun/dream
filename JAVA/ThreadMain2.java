
public class ThreadMain2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Runnable task = () -> {//Runnable�� ���θ޼��忡�� ���ٽ����� �����ؼ� �����忡 �־� ���.
			for(int i = 0; i < 5; i++) {
				System.out.println("�߰�.");
				try {
					Thread.sleep(500);
				} catch (Exception e) {
					// TODO: handle exception
				}
			}
		};
		
		Thread th = new Thread(task);
		th.start();
		
		for(int i = 0; i < 5; i++) {
			System.out.println("�ȳ�.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		
		
	}

}
