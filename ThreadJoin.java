class JoinThread extends Thread{
	int total;
	public void run() {
		for (int i=1; i<=100;i++) {
			total += i;
		}
	}
}

public class ThreadJoin {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		JoinThread t = new JoinThread();
		t.start();
		
		try {
			t.join();//������ ��� �����Ҷ����� �Ʒ� ó�� ���.
			System.out.println("������ t�� ���� ������ ���...");
		} catch (Exception e) {
			// TODO: handle exception
		}
		
		System.out.println("���� : "+t.total);
		
		
	}

}
