
public class ThreadMain3 {

	public static void main(String[] args) {//������ Ŭ������ ��ӹ��� Ŭ������ ���� ���� runable�������̽��� ������� �ʰ� �ٷ� ���.
		// TODO Auto-generated method stub
		Thread th = new SubThread();
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

class SubThread extends Thread {
	public void run() {
		for(int i = 0; i < 5; i++) {
			System.out.println("�߰�.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
	}
}