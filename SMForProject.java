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
	String host = "smtp.naver.com"; // 네이버일 경우 네이버 계정, gmail경우 gmail 계정
	String user = "tlstmdrbsdustmq@naver.com"; // 패스워드
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

	public void sendMail1(String to, String title, String mainText) {// 1명에게 메일 보내는 함수
		try {
			MimeMessage message = new MimeMessage(session);
			message.setFrom(new InternetAddress(user));

			message.addRecipient(Message.RecipientType.TO, new InternetAddress(to));// 1인용

			// 메일 제목
			message.setSubject(title);
			// 메일 내용
			message.setText(mainText);
			// send the message
			Transport.send(message);
			System.out.println("Success Message Send");

		} catch (MessagingException e) {
			e.printStackTrace();
		}

	}
	public void sendAllMail(List<String> toList, String title, String mainText) {//다인용
		try { 
			MimeMessage message = new MimeMessage(session); 
			message.setFrom(new InternetAddress(user));
			
			InternetAddress[] addArray = new InternetAddress[toList.size()]; 
			for(int i = 0; i<toList.size(); i++) {
				addArray[i] = new InternetAddress(toList.get(i));
			}
			message.addRecipients(Message.RecipientType.TO, addArray);
			// 메일 제목
			message.setSubject(title); 
			// 메일 내용
			message.setText(mainText); 
			// send the message 
			Transport.send(message); 
			System.out.println("Success Message Send");

		} catch (MessagingException e) { 
			e.printStackTrace(); 
		}
		
		
		
		
	}
}
