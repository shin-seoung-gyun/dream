package JavaQuiz;

public class JavaQuiz02 {

	public static void main(String[] args) {
		//[����2]65430���� ����� ���� ȭ���� ������ ���Ͻÿ�.
		//money = 65430��
		int money = 65430;
		int ten = money/10%10;
		System.out.println("�ʿ� = "+ten);
		int hun = money/100%10;
		System.out.println("��� = "+hun);
		int thousand = money/1000%10;
		System.out.println("õ�� = "+thousand);
		int tenthousand = money/10000%10;
		System.out.println("���� = "+tenthousand);
	}

}
