
public class ThreadInterrupt1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Runnable task = () -> {
			try {
				while(true) {
					System.out.println("������...");
					Thread.sleep(1);
				}
				
				
			} catch (InterruptedException e) {//���ͷ�Ʈ ó���ڵ�
				// TODO: handle exception
			}
			System.out.println("���� ����");
		};// �������̽��� �ٷ� ���ٽ����� ����Ͽ� �����ݷ����� �ݾ������.
		
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
