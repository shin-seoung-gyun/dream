import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadMain5 {

	public static void main(String[] args) throws InterruptedException, ExecutionException {
		// TODO Auto-generated method stub
		Runnable task = () -> {
			for(int i = 0 ; i <5; i++) {
				System.out.println("잘가.");
				try {
					Thread.sleep(500);
				} catch (Exception e) {
					// TODO: handle exception
				}
			}
			
		};
//		ExecutorService exec = Executors.newCachedThreadPool();//스레드 풀 을 생성하는 두가지 방법 이경우는 제한없이 스레드풀이 넓어진다 이론상으로
		ExecutorService exec = Executors.newFixedThreadPool(4);//이 스레드풀은 생성할때 생성스레드 개수를 지정한다 진행되지 않는 스레드가 있어도 정해진개수 아래로 내려가지 않는다.
//		exec.execute(task);//리턴값이 보이드
		var fu = exec.submit(task);//리턴값 퓨처 리턴값으로 여러가지 메서드를 사용하여 제어할수있음
		System.out.println(fu.isDone());
		System.out.println(fu.get());
		System.out.println(fu.isDone());
		for(int i = 0 ; i <5; i++) {
			System.out.println("안녕.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}	
		
		
	}

}
