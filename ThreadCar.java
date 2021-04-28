
class CarThread extends Thread{
	private String who;
	private ThreadSynchronized car;
	private String where;
	
	public CarThread(String who, ThreadSynchronized car, String where) {
		super();
		this.who = who;
		this.car = car;
		this.where = where;
	}
	public void run() {
		car.drive(who, where);
	}
}

public class ThreadCar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ThreadSynchronized car = new ThreadSynchronized();
		new CarThread("»«Áö¸®",car,"¼­¿ï").start();
		new CarThread("¹®µÕÀÌ",car,"ºÎ»ê").start();
		new CarThread("²¤²¤ÀÌ",car,"±¤ÁÖ").start();
		
		
		
		
		
	}

}
