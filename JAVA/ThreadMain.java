

public class ThreadMain {

	public static void main(String[] args) {// Runnable을 상속받은 클래스를 만들어서 스레드를 객체화 한후 받아서 실행.
		// TODO Auto-generated method stub
		IntegerStore is = new IntegerStore(0);
		
		Thread t = new Thread(new MyRunnable(is));
//		Thread t2 = new Thread(new MyRunnable(is));
		t.setDaemon(true);
		t.start();
//		t2.start();
		for(int i = 0; i < 5; i++) {
			System.out.println("안녕.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
			
		}
		
		System.out.println(is.num);
		
	}
	
}

class MyRunnable implements Runnable {//스레드 객체 생성하여 실행할 스레드 처리
	IntegerStore is;
	public MyRunnable(IntegerStore is) {
		this.is = is;
	}
	
	public void run() {
		for(int i =0; i<10;i++) {
			System.out.println("잘가.");
//			synchronized (is) {
//				is.num++;
//			}
			
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				// TODO: handle exception
			}
		}
	}
}


class IntegerStore {
	int num=0;
	public IntegerStore(int num) {
		// TODO Auto-generated constructor stub
		this.num = num;
	}
	
}
