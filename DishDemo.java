
public class DishDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		final Dish d = new Dish();
		new Thread(new Customer(d)).start();
		new Thread(new Cook(d)).start();
	}

}
