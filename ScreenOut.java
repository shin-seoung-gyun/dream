
public class ScreenOut {
	static void menu() {
		System.out.println("-----------------------------------");
		System.out.println("\t�뵷 ������\n");
		System.out.println("\t1.���� �Է�");
		System.out.println("\t2.���� �Է�");
		System.out.println("\t3.�ܾ� Ȯ��");
		System.out.println("\t4.��ü ��ȸ");
		System.out.println("\t5.�������Է� ���");
		System.out.println("\t6.����� 1~3�� ��ȸ");
		System.out.println("\t7.�Ⱓ�� �����հ� �����հ� ��ȸ");
		System.out.println("\t8.�Ⱓ�� ������� ������� ��ȸ");
		System.out.println("\t9.�Ϻ� ����,���� ��ȸ");
		System.out.println("\t0.����\n");
		System.out.println("\t �޴���ȣ�� �Է��ϼ���.");
		System.out.println("-----------------------------------");
		System.out.print("�Է� > ");

	}
	static void startDay() {
		System.out.println("\t�������� �Է��ϼ���.\n\tex) 2000-01-23.");
		System.out.print("�Է� > ");
	}
	static void endDay() {
		System.out.println("\t�������� �Է��ϼ���.\n\tex) 2000-01-23.");
		System.out.print("�Է� > ");
	}

	static void outItem() {
		System.out.println("\t������ ������ �Է��ϼ���.\n\tex) ����, �������� ��.");
		System.out.print("�Է� > ");
	}

	static void inItem() {
		System.out.println("\t���� ������ �Է��ϼ���.\n\tex) ����, �뵷 ��.");
		System.out.print("�Է� > ");
	}

	static void outMoney() {
		System.out.println("\t������ �ݾ��� �Է��ϼ���.\n\tex) 1000, 30000 ��.");
		System.out.print("�Է� > ");
	}

	static void inMoney() {
		System.out.println("\t���� �ݾ��� �Է��ϼ���.\n\tex) 1000, 30000 ��.");
		System.out.print("�Է� > ");
	}

	static void checkMent(String item, String money, String inOut) {
		System.out.println("\t" + item + "��(��)" + money + "�� ��ŭ " + inOut + "�� �½��ϱ�?");
		System.out.println("\t1)��\t2)�ƴϿ�");
		System.out.print("�Է� > ");
	}
	static void checkDayMent(String item, String money, String inOut) {
		System.out.println("\t" + item + "�� ����" + money + "�� ���� " + inOut + "�� �½��ϱ�?");
		System.out.println("\t1)��\t2)�ƴϿ�");
		System.out.print("�Է� > ");
	}

	static void yesMent() {
		System.out.println("\tȮ�� �Ǿ����ϴ�.");
	}

	static void noMent() {
		System.out.println("\t��� �Ǿ����ϴ�.");
	}

}
