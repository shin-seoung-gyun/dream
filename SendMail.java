import java.util.Properties;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;


public class SendMail {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String host = "smtp.naver.com"; // ���̹��� ��� ���̹� ����, gmail��� gmail ���� 
		String user = "tlstmdrbsdustmq@naver.com"; // �н����� 
		String password = "dustmqdydapdlf";
		
		// SMTP ���� ������ �����Ѵ�. 
		Properties props = new Properties(); 
		props.put("mail.smtp.host", host); 
		props.put("mail.smtp.port", 587); 
		props.put("mail.smtp.auth", "true");
		
		Session session = Session.getDefaultInstance(props, new javax.mail.Authenticator() { 
			protected PasswordAuthentication getPasswordAuthentication() { 
				return new PasswordAuthentication(user, password); 
				} 
		});

		try { 
			MimeMessage message = new MimeMessage(session); 
			message.setFrom(new InternetAddress(user));
			
			InternetAddress[] addArray = new InternetAddress[2]; //���ο�
			addArray[0] = new InternetAddress("tlstmdrbsdustmq@naver.com"); 
			addArray[1] = new InternetAddress("sg0220.shin@daum.net"); 
	
			message.addRecipients(Message.RecipientType.TO, addArray);
			//message.addRecipient(Message.RecipientType.TO, new InternetAddress("seolmuah@naver.com"));//1�ο�
			
			// ���� ����
			message.setSubject("�׽�Ʈ �����Դϴ�."); 
			// ���� ����
			message.setText("������ �м� �����Դϴ�."); 
			// send the message 
			Transport.send(message); 
			System.out.println("Success Message Send");

		} catch (MessagingException e) { 
			e.printStackTrace(); 
		}

	}

}
