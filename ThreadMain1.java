
public class ThreadMain1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Thread(new Runnable() {//��üȭ ���� �ʰ� �ٷ� �͸� ������� ����
			public void run() {
				for(int i = 0; i<5; i++) {
					System.out.println("�߰�");
					try {
						Thread.sleep(500);
					} catch (Exception e) {
						// TODO: handle exception
					}
				}
				
			}
		}).start();//�ٷ� start�� �ٿ��� ����.
		
		for(int i = 0; i<5; i++) {
			System.out.println("�ȳ�.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		
		
		
	}

}
