import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		OutLine ot = new OutLine();
		Scanner in = new Scanner(System.in);
		DBAccess da = new DBAccess();
		RMForProject rm = new RMForProject();
		Date date = new Date();
		SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		
		while (true) {
			ot.menu();
			System.out.print("�޴��� �Է��ϼ���.>");
			String userStr = in.nextLine();

			// �ּҷϺ���
			if (userStr.equals("1")) {
				ot.menu2();
				System.out.print("�޴��� �Է��ϼ���.>");
				String userStr2 = in.nextLine();

				if (userStr2.equals("1")) {
					System.out.println("\t��ü �ּҷ��� �ҷ��ɴϴ�.");
					da.allAddress();// ��� �ּҷ� �ҷ����� �Լ�
				} else if (userStr2.equals("2")) {
					System.out.println("\t�̸����� �˻��� �����մϴ�.");
					// �̸����� �˻��ϴ� �Լ�
					System.out.print("�̸��� �Է��� �ּ���.>");
					String name = in.nextLine();
					da.findNameAddress(name);
				} else if (userStr2.equals("3")) {
					System.out.println("\t�Ҽ����� �˻��� �����մϴ�.");
					// �Ҽ����� �˻��ϴ� �Լ�
					System.out.print("�Ҽ��� �Է��� �ּ���.>");
					String Affiliation = in.nextLine();
					da.findAffiliationAddress(Affiliation);
				} else {
					System.out.println("\t�߸��Է��ϼ̽��ϴ�. ó������ ���ư��ϴ�.");
					continue;
				}

			} else if (userStr.equals("2")) {// ���Ϻ�����
				ot.menu3();
				System.out.print("�޴��� �Է��ϼ���.>");
				String userStr2 = in.nextLine();

				// �Ѹ��� ���� ����
				if (userStr2.equals("1")) {
					System.out.println("\t�Ѹ��� ������ �����ϴ�.");
					// �Ѹ��� ���� ���� ó��
					SMForProject sp = new SMForProject();
					System.out.print("�޴� ���� ���� �ּҸ� �Է��ϼ���.>");
					String reID = in.nextLine();
					// �ش� ���̵� �ּҷϿ� ������ ������ �⺻���� ���
					System.out.print("����>");
					String title = in.nextLine();
					System.out.print("����>");
					String mainText = in.nextLine();
					// ���̵� ���� ������ ã�� �Լ� �ʿ�.
					boolean sameAddress = da.isTure(reID);
					if (sameAddress == false) {
						sp.sendMail1(reID, title, mainText);
					} else {
						sp.sendMail1(reID, title, da.baseText(mainText, reID));
					}
					da.sendMail(reID, title, mainText, format.format(date));
					
					// �������� ���Ϻ��� ó��
				} else if (userStr2.equals("2")) {
					System.out.println("\t����������� ������ �����ϴ�.");
					ot.menu4();
					System.out.print("�޴��� �Է��ϼ���.>");
					String userStr3 = in.nextLine();

					if (userStr3.equals("1")) {// �ּҷ� ��ü ������
						System.out.println("��ü ���� �߼��մϴ�.");
						
						SMForProject sp = new SMForProject();
						System.out.print("����>");
						String title = in.nextLine();
						System.out.print("����>");
						String mainText = in.nextLine();
						// ��ü �ּҷ��� email�� List�� �ҷ����� �Լ�
						List<String> toList = da.allAddAry();
						// ���� �Լ����� �޾ƿ� ���� �ּҷ� �Ѹ��� �Լ�
						sp.sendAllMail(toList, title, mainText);
						for(int i = 0; i <toList.size();i++) {
							da.sendMail(toList.get(i), title, mainText, format.format(date));
						}

					} else if (userStr3.equals("2")) {// �Ҽ� ��ü������
						System.out.println("�Ҽ� �׷�߼��մϴ�.");
						
						System.out.print("�����ô� ���� �Ҽ��� �Է��ϼ���.>");
						String reAffiliation = in.nextLine();
						SMForProject sp = new SMForProject();
						System.out.print("����>");
						String title = in.nextLine();
						System.out.print("����>");
						String mainText = in.nextLine();
						List<String> emailList = da.findAffAdd(reAffiliation);//�Ҽ����� �̸��ϸ���Ʈ�� �޾ƿ��� �Լ�
						for (int i = 0; i < emailList.size(); i++) {
							sp.sendMail1(emailList.get(i), title, da.baseText(mainText, emailList.get(i)));
							da.sendMail(emailList.get(i), title, mainText, format.format(date));
						}

					} else if (userStr3.equals("3")) {// �Ҽ� �� �μ� �Է��� ��� ������
						System.out.println("�Ҽӹ� �μ� �׷�߼��մϴ�.");
						System.out.print("�����ô� ���� �Ҽ��� �Է��ϼ���.>");
						String reAffiliation = in.nextLine();
						System.out.print("�����ô� ���� �μ��� �Է��ϼ���.>");
						String divisions = in.nextLine();
						SMForProject sp = new SMForProject();
						System.out.print("����>");
						String title = in.nextLine();
						System.out.print("����>");
						String mainText = in.nextLine();
						List<String> emailList = da.findAffDivAdd(reAffiliation, divisions);//�Ҽӹ� �μ��� �̸��ϸ���Ʈ�� �޾ƿ��� �Լ�
						for (int i = 0; i < emailList.size(); i++) {
							sp.sendMail1(emailList.get(i), title, da.baseText(mainText, emailList.get(i)));
							da.sendMail(emailList.get(i), title, mainText, format.format(date));
						}
					} else {
						System.out.println("\t�߸��Է��ϼ̽��ϴ�. ó������ ���ư��ϴ�.");
						continue;
					}

				} else {
					System.out.println("\t�߸��Է��ϼ̽��ϴ�. ó������ ���ư��ϴ�.");
					continue;
				}
			//���� ���� Ȯ���ϱ�
			} else if (userStr.equals("3")) {
				ot.menu5();
				System.out.print("�޴��� �Է��ϼ���.>");
				String userStr2 = in.nextLine();
				if (userStr2.equals("1")){//��ü ���� Ȯ��
					System.out.println("��ü ���� ���� 10���� ����մϴ�");
					try {
						rm.reciveAllMail();
					} catch (Exception e) {
						// TODO: handle exception
						e.printStackTrace();
					}
				} else if (userStr2.equals("2")) {//���� ���� ���� Ȯ��
					System.out.println("�������� ���� ���� ���� 10���� ����մϴ�");
					try {
						rm.reciveMail();
					} catch (Exception e) {
						// TODO: handle exception
						e.printStackTrace();
					}
				}
			//���� ���� Ȯ���ϱ�	
			} else if (userStr.equals("4")) {	
				System.out.println("���� ������ ����մϴ�.");
				da.findSendMail();
				
			} else if (userStr.equals("5")) {	//�ּҷ� �߰�
				System.out.println("�ּҷ��� �߰��մϴ�.");
				System.out.print("�̸��� �Է��ϼ���>");
				String name = in.nextLine();
				System.out.print("�Ҽ��� �Է��ϼ���>");
				String affiliation = in.nextLine();
				System.out.print("�μ��� �Է��ϼ���>");
				String divisions = in.nextLine();
				System.out.print("������ �Է��ϼ���>");
				String position = in.nextLine();
				System.out.print("����ó�� �Է��ϼ���>");
				String phone = in.nextLine();
				System.out.print("�̸����ּҸ� �Է��ϼ���>");
				String eMail = in.nextLine();
				da.insertAB(name, divisions, position, phone, eMail, affiliation);
				
			} else if (userStr.equals("6")) {	// �ּҷ� ���� (no�� ������ Į���� �ϳ��� �Է¹ް� ������ ���� �Է¹��� �� ����)	
				System.out.println("�ּҷ��� �����մϴ�.");
				System.out.println("�ּҷ��� ��ȣ�� �Է��ϼ���>");
				int no = in.nextInt();
				in.nextLine();
				System.out.println("������ Į���� �Է��ϼ���. ex)�̸�,�Ҽ�,����,�μ�,����ó,�̸����ּ�>");
				String column = in.nextLine();
				System.out.println("������ ������ �Է��ϼ���>");
				String text = in.nextLine();
				da.setColumn(no, column, text);
				
			} else if (userStr.equals("7")) {	// �ּҷ� ���� (no �Է¹ް� �ش� no �� ����)	
				System.out.println("�ּҷ��� �����մϴ�.");
				System.out.println("�ּҷ��� ��ȣ�� �Է��ϼ���>");
				int no = in.nextInt();
				in.nextLine();
				da.deleteDate(no);
				
			} else if (userStr.equals("0")) {//����
				System.out.println("\t���α׷��� �����մϴ�.");
				break;
			}

		}

	}

}
