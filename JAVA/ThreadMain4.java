
public class ThreadMain4 {

	public static void main(String[] args) {//runable �������̽� ��������ʰ� �ٷ� �͸� ������ ��ü �ȿ� void run�ż��带 ���� ���.
		// TODO Auto-generated method stub
		new Thread() {public void run(){
			for(int i = 0; i <5; i++) {
				System.out.println("�߰�.");
				try {
					Thread.sleep(500);
				} catch (Exception e) {
					// TODO: handle exception
				}
			}
		}}.start();
		
		for(int i = 0; i <5; i++) {
			System.out.println("�ȳ�.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		

	}

}
