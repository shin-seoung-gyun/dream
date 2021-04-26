import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Database db = new Database();
		Scanner in = new Scanner(System.in);
		System.out.print("이름을 입력하세요. > ");
		String name = in.nextLine();

		db.selectAllFromName(name);

	}

}
