import java.text.SimpleDateFormat;

import javax.mail.Message;

public class RMForProject {
	String host = "imap.naver.com"; // imap ȣ��Ʈ �ּ�. ex) imap.gmail.com
	String userEmail = "tlstmdrbsdustmq@naver.com"; // ���� �̸��� �ּ�
	String password = "dustmqdydapdlf"; // ���� ��ȣ
	IMAPMailService mailService = new IMAPMailService();

	public void reciveMail() throws Exception {//
		DBAccess da = new DBAccess();
		mailService.login(host, userEmail, password);
		int messageCount = mailService.getMessageCount();
		// �׽�Ʈ �����̶� 5�� �ʰ��̸� 5���� ó��: TODO ����
		if (messageCount > 10) {
			messageCount = 10;
		}
		Message[] msgArray = mailService.getMessages(true);
		for (int i = 0; i < messageCount; i++) {
			Message msg = msgArray[i];
			
			if (msg.getSubject() != null) {
				System.out.println("-------------------------------------------------------");
				// System.out.println(String.format("������Ÿ��: %s", msg.getContentType()));
				SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
				String sendor = msg.getFrom()[0].toString();
				int lastIdx = (sendor.indexOf("<") == -1) ? sendor.length() : sendor.length() - 1;
				sendor = sendor.substring(sendor.indexOf("<") + 1, lastIdx);
				System.out.println(String.format("�߽���: %s", sendor));
				// �߽���(�̸����ּ�)�� �̸� �Ҽ� �μ� �� �޾ƿ��� �Լ� �ʿ�
				String[] strAry = da.findEMail2(sendor);
				System.out.println(String.format("�߽��� �̸�: %s", strAry[0]));
				System.out.println(String.format("�߽��� �Ҽ�: %s", strAry[1]));
				System.out.println(String.format("�߽��� �μ�: %s", strAry[2]));
				System.out.println(String.format("��������: %s", msg.getSubject()));
				System.out.println(String.format("���Ϲ߼۽ð�: %s", format.format(msg.getSentDate())));
				System.out.println("�������� :" + msg.getFlags());
				// �̸� �Ҽ� �μ� �߰��ؾ���.
//	                 String mailText = mailService.getEmalText(msg.getContent());
//	                 System.out.println(String.format("���ϳ���: %s", mailText));
			}
		}
		mailService.logout(); // �α׾ƿ�
	}

	public void reciveAllMail() throws Exception {// try������ ��������ʾƼ� �ʿ��Ѱǰ�?
		DBAccess da = new DBAccess();
		mailService.login(host, userEmail, password);
		int messageCount = mailService.getMessageCount();
		// �׽�Ʈ �����̶� 5�� �ʰ��̸� 5���� ó��: TODO ����
		if (messageCount > 10) {
			messageCount = 10;
		}
		Message[] msgArray = mailService.getMessages(false);
		for (int i = 0; i <messageCount; i++) {
			Message msg = msgArray[i];
			
			if (msg.getSubject() != null) {
				System.out.println("-------------------------------------------------------");
				// System.out.println(String.format("������Ÿ��: %s", msg.getContentType()));
				SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
				String sendor = msg.getFrom()[0].toString();
				int lastIdx = (sendor.indexOf("<") == -1) ? sendor.length() : sendor.length() - 1;
				sendor = sendor.substring(sendor.indexOf("<") + 1, lastIdx);
				System.out.println(String.format("�߽���: %s", sendor));
				// �߽���(�̸����ּ�)�� �̸� �Ҽ� �μ� �� �޾ƿ��� �Լ� �ʿ�
				String[] strAry = da.findEMail2(sendor);
				System.out.println(String.format("�߽��� �̸�: %s", strAry[0]));
				System.out.println(String.format("�߽��� �Ҽ�: %s", strAry[1]));
				System.out.println(String.format("�߽��� �μ�: %s", strAry[2]));
				System.out.println(String.format("��������: %s", msg.getSubject()));
				System.out.println(String.format("���Ϲ߼۽ð�: %s", format.format(msg.getSentDate())));
				System.out.println("�������� :" + msg.getFlags());
				// �̸� �Ҽ� �μ� �߰��ؾ���.
//	                 String mailText = mailService.getEmalText(msg.getContent());
//	                 System.out.println(String.format("���ϳ���: %s", mailText));
			}
		}
		mailService.logout(); // �α׾ƿ�
	}

}
