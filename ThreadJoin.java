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
			t.join();//스레드 모두 종료할때까지 아래 처리 대기.
			System.out.println("스레드 t가 끝날 때까지 대기...");
		} catch (Exception e) {
			// TODO: handle exception
		}
		
		System.out.println("총합 : "+t.total);
		
		
	}

}
