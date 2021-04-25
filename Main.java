
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		DBAccess da = new DBAccess();// Ŭ���� ����Ʈ
		SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
		Date date = new Date();
		while (true) {

			ScreenOut.menu();
			switch (in.nextLine()) {
			case "1":// ����
			{
				ScreenOut.outItem();
				String item = in.nextLine();
				ScreenOut.outMoney();
				String money = in.nextLine();
				ScreenOut.checkMent(item, money, "����");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					String strDate = format.format(date).toString();
					da.insertRow(item, "-" + money,strDate);// INSERT DATA �Լ� �ʿ� �������̶� -�߰�
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;
			}
			case "2":// ����
			{
				ScreenOut.inItem();
				String item = in.nextLine();
				ScreenOut.inMoney();
				String money = in.nextLine();
				ScreenOut.checkMent(item, money, "����");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					String strDate = format.format(date).toString();
					da.insertRow(item, money,strDate);// INSERT DATA �Լ� �ʿ�//abs?
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;

			}
			case "3":// �ܾ�
			{
				int sumMoney = da.getMoneyBalance();// �ܾ� ����� �������� �Լ� �ʿ�
				System.out.println("\t���糲�� �ݾ��� " + sumMoney + "�� �Դϴ�.");
				System.out.println("Enter");
				in.nextLine();
				break;
			}

			case "4":// ��ü��ȸ
			{
				System.out.println("\t��ü ����� ��ȸ�մϴ�.");
				System.out.println("Enter");
				in.nextLine();
				System.out.println("\t����(����)����\t�ݾ�\t\t��¥.");
				System.out.println("\t************************************");
				var listItem = da.selectAllItem();// ��ü ��ȸ �� �������� �Լ� �ʿ�
				for (var item : listItem) {// for�� Ȱ�� ���� ǥ��
					System.out.print("\t" + item.item);
					if (item.item.length() < 7) {
						System.out.print("\t");
					}

					System.out.print("\t" + item.money);
					if (item.money.length() < 10) {
						System.out.print("\t");
					}

					SimpleDateFormat format1 = new SimpleDateFormat("yyyy-MM-dd");
					System.out.print("\t" + format1.format(item.date1) + "\n");// ������ ����ƮŸ������ ����ȯ �ʿ�

				}
				break;
			}

			case "5":// ������ �Է� ���
			{
				System.out.println("\t������ �Է��� ����մϴ�.");
				System.out.println("Enter");
				in.nextLine();
				da.lastOrderCancle();
				break;
			}
			case "6":// ����� 1~3�� ��ȸ
			{
				System.out.println("\t����� 1~3���� ��ȸ�մϴ�.");
				System.out.println("Enter");
				in.nextLine();

				System.out.println("\t���⳻��\t\t�ݾ�.");
				System.out.println("\t************************************");

				var rankItem = da.outPocket();// ��ü ��ȸ �� �������� �Լ� �ʿ�
				for (var item1 : rankItem) {// for�� Ȱ�� ���� ǥ��
					System.out.print("\t" + item1.item);
					if (item1.item.length() < 7) {
						System.out.print("\t");
					}
					System.out.print("\t" + item1.money + "\n");

				}

			}
			case "7": {
				System.out.println("\t�Ⱓ�� �����հ�, �����հ踦 ��ȸ�մϴ�.");
				ScreenOut.startDay();
				String start = in.nextLine();
				ScreenOut.endDay();
				String end = in.nextLine();
				System.out.println("Enter");
				in.nextLine();
				
				ScreenOut.checkDayMent(start, end, "�Ⱓ");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					System.out.println("\t�Ѽ��Գ���\t\t�����⳻��.");
					System.out.println("\t************************************");

					var listDaily = da.dailyInOut(start, end);
					for (var item2 : listDaily) {// for�� Ȱ�� ���� ǥ��
						System.out.print("\t" + item2.item);//�Ѽ���
						if (item2.item.length() < 7) {
							System.out.print("\t");
						}
						System.out.print("\t\t" + item2.money + "\n");//������
					}
					
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;
			}
			
			case "8": {
				System.out.println("\t�Ⱓ�� �������, ������ո� ��ȸ�մϴ�.");
				ScreenOut.startDay();
				String start = in.nextLine();
				ScreenOut.endDay();
				String end = in.nextLine();
				System.out.println("Enter");
				in.nextLine();
				
				ScreenOut.checkDayMent(start, end, "�Ⱓ");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					System.out.println("\t������ճ���\t\t������ճ���.");
					System.out.println("\t************************************");

					var listDailyAvg = da.dailyInOutAvg(start, end);
					for (var item2 : listDailyAvg) {// for�� Ȱ�� ���� ǥ��
						System.out.print("\t" + item2.item);//�Ѽ���
						if (item2.item.length() < 7) {
							System.out.print("\t");
						}
						System.out.print("\t\t" + item2.money + "\n");//������
					}
					
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;
			}
			
			case "9": {
				System.out.println("\t�Ϻ� ����, ���⸦ ��ȸ�մϴ�.");
				ScreenOut.startDay();
				String start = in.nextLine();
				ScreenOut.endDay();
				String end = in.nextLine();
				System.out.println("Enter");
				in.nextLine();
				
				ScreenOut.checkDayMent(start, end, "�Ⱓ");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					System.out.println("\t����,���⳻��\t\t����.");
					System.out.println("\t************************************");

					var dailyListMoney = da.dailyInOutMoney(start, end);
					for (var item2 : dailyListMoney) {// for�� Ȱ�� ���� ǥ��
						System.out.print("\t" + item2.item);//���� ����
						if (item2.item.length() < 10) {
							System.out.print("\t");
						}
						SimpleDateFormat format1 = new SimpleDateFormat("yyyy-MM-dd");
						System.out.print("\t\t" + format1.format(item2.date1) + "\n");//����
					}
					
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;
			}

			case "0":// ����
			{
				System.out.println("����Ǿ����ϴ�.");
				return;
			}
			default:
				System.out.println("�߸��Է��ϼ̽��ϴ�. �ٽ� �Է��ϼ���");
				break;

			}
		}
	}

}
