import java.text.SimpleDateFormat;

import javax.mail.Message;

public class receiveMail {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		// TODO Auto-generated method stub
				System.out.println("-- IMAP Emal ��������: Start\n\n");
		        String host = "imap.naver.com"; //imap ȣ��Ʈ �ּ�. ex) imap.gmail.com
		        String userEmail = "tlstmdrbsdustmq@naver.com"; //���� �̸��� �ּ�
		        String password = "dustmqdydapdlf"; //���� ��ȣ
		        IMAPMailService mailService = new IMAPMailService();
		        mailService.login(host, userEmail, password);
		        int messageCount = mailService.getMessageCount();
		        //�׽�Ʈ �����̶� 5�� �ʰ��̸� 5���� ó��: TODO ����
		        if (messageCount > 5) {
		             //messageCount = 5;
		        }
		        Message[] msgArray = mailService.getMessages(false);
		        for (int i = 0; i < msgArray.length; i++) {
		             Message msg = msgArray[i];
		             if (msg.getSubject() != null) {
		            	 System.out.println("-------------------------------------------------------");
			             //System.out.println(String.format("������Ÿ��: %s", msg.getContentType()));
		            	 SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
		            	 String sendor = msg.getFrom()[0].toString();
		            	 int lastIdx = (sendor.indexOf("<")==-1) ? sendor.length():sendor.length()-1;
		            	 sendor = sendor.substring(sendor.indexOf("<")+1, lastIdx);
		            	 System.out.printf("���Ϲ�ȣ: %d\n", i);
			             System.out.println(String.format("�߽���: %s", sendor));
			             System.out.println(String.format("��������: %s", msg.getSubject()));
			             System.out.println(String.format("���Ϲ߼۽ð�: %s", format.format(msg.getSentDate())));
			             System.out.println("�������� :" + msg.getFlags());
			             
//		                 String mailText = mailService.getEmalText(msg.getContent());
//		                 System.out.println(String.format("���ϳ���: %s", mailText));
		             }
		        }
		        mailService.logout(); //�α׾ƿ�
		        System.out.println("\n\n-- IMAP Emal ��������: ����");
	}

}
