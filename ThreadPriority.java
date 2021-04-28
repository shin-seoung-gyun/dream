class Counter extends Thread{
	private int count =0;
	public Counter(String name) {
		setName(name);
	}
	public void run() {
		while(count++<5) {
			System.out.print(getName() + "->");
			try {
				sleep(500);
			} catch (InterruptedException e) {
				// TODO: handle exception
			}
		}
	}
}

public class ThreadPriority {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Counter c1 = new Counter("´À±ßÇÑ");
		c1.setPriority(Thread.MIN_PRIORITY);
		Counter c2 = new Counter("±ÞÇÑ");
		c2.setPriority(Thread.MAX_PRIORITY);
		c1.start();
		c2.start();
		
		
		
		
		
		
		
		
		
		
		
		
		

	}

}
