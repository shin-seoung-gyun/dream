
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
		System.out.println("������ �Է��ϼ���.");
		String gend = in.nextLine();
		gender = gend.charAt(0);
		System.out.println("������ �Է��ϼ���.");
		tall = in.nextDouble();
		System.out.println("ü���� �Է��ϼ���.");
		weight = in.nextDouble();
	
	}
	public void output() {
		System.out.printf("���� : %s\n���� : %.2f\nü�� : %.2f",gender,tall,weight);
	}
	
	
}
