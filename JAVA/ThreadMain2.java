
public class ThreadMain2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Runnable task = () -> {//Runnable을 메인메서드에서 람다식으로 정의해서 스레드에 넣어 사용.
			for(int i = 0; i < 5; i++) {
				System.out.println("잘가.");
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
			System.out.println("안녕.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}
		
		
	}

}
