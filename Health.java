
import java.util.Scanner;

public class Health {
	char gender;
	double tall;
	double weight;
	
	public Health() {
		super();
	}

	public Health(char gender, double tall, double weight) {
		super();
		this.gender = gender;
		this.tall = tall;
		this.weight = weight;
	}
	
	public void input() {
		Scanner in = new Scanner(System.in);
		System.out.println("성별을 입력하세요.");
		String gend = in.nextLine();
		gender = gend.charAt(0);
		System.out.println("신장을 입력하세요.");
		tall = in.nextDouble();
		System.out.println("체중을 입력하세요.");
		weight = in.nextDouble();
	
	}
	public void output() {
		System.out.printf("성별 : %s\n신장 : %.2f\n체중 : %.2f",gender,tall,weight);
	}
	
	
}
