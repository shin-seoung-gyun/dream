import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Database db = new Database();
		Scanner in = new Scanner(System.in);
		System.out.print("�̸��� �Է��ϼ���. > ");
		String name = in.nextLine();

		db.selectAllFromName(name);

	}

}
