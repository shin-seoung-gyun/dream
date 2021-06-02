import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadMain5 {

	public static void main(String[] args) throws InterruptedException, ExecutionException {
		// TODO Auto-generated method stub
		Runnable task = () -> {
			for(int i = 0 ; i <5; i++) {
				System.out.println("�߰�.");
				try {
					Thread.sleep(500);
				} catch (Exception e) {
					// TODO: handle exception
				}
			}
			
		};
//		ExecutorService exec = Executors.newCachedThreadPool();//������ Ǯ �� �����ϴ� �ΰ��� ��� �̰��� ���Ѿ��� ������Ǯ�� �о����� �̷л�����
		ExecutorService exec = Executors.newFixedThreadPool(4);//�� ������Ǯ�� �����Ҷ� ���������� ������ �����Ѵ� ������� �ʴ� �����尡 �־ ���������� �Ʒ��� �������� �ʴ´�.
//		exec.execute(task);//���ϰ��� ���̵�
		var fu = exec.submit(task);//���ϰ� ǻó ���ϰ����� �������� �޼��带 ����Ͽ� �����Ҽ�����
		System.out.println(fu.isDone());
		System.out.println(fu.get());
		System.out.println(fu.isDone());
		for(int i = 0 ; i <5; i++) {
			System.out.println("�ȳ�.");
			try {
				Thread.sleep(500);
			} catch (Exception e) {
				// TODO: handle exception
			}
		}	
		
		
	}

}
