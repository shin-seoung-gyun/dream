import java.util.Arrays;
import java.util.List;
import java.util.Properties;

import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class SMForProject {
	String host = "smtp.naver.com"; // ���̹��� ��� ���̹� ����, gmail��� gmail ����
	String user = "tlstmdrbsdustmq@naver.com"; // �н�����
	String password = "dustmqdydapdlf";
	Session session;

	public SMForProject() {
		Properties props = new Properties();
		props.put("mail.smtp.host", host);
		props.put("mail.smtp.port", 587);
		props.put("mail.smtp.auth", "true");

		session = Session.getDefaultInstance(props, new javax.mail.Authenticator() {
			protected PasswordAuthentication getPasswordAuthentication() {
				return new PasswordAuthentication(user, password);
			}
		});
	}

	public void sendMail1(String to, String title, String mainText) {// 1���� ���� ������ �Լ�
		try {
			MimeMessage message = new MimeMessage(session);
			message.setFrom(new InternetAddress(user));

			message.addRecipient(Message.RecipientType.TO, new InternetAddress(to));// 1�ο�

			// ���� ����
			message.setSubject(title);
			// ���� ����
			message.setText(mainText);
			// send the message
			Transport.send(message);
			System.out.println("Success Message Send");

		} catch (MessagingException e) {
			e.printStackTrace();
		}

	}
	public void sendAllMail(List<String> toList, String title, String mainText) {//���ο�
		try { 
			MimeMessage message = new MimeMessage(session); 
			message.setFrom(new InternetAddress(user));
			
			InternetAddress[] addArray = new InternetAddress[toList.size()]; 
			for(int i = 0; i<toList.size(); i++) {
				addArray[i] = new InternetAddress(toList.get(i));
			}
			message.addRecipients(Message.RecipientType.TO, addArray);
			// ���� ����
			message.setSubject(title); 
			// ���� ����
			message.setText(mainText); 
			// send the message 
			Transport.send(message); 
			System.out.println("Success Message Send");

		} catch (MessagingException e) { 
			e.printStackTrace(); 
		}
		
		
		
		
	}
}
