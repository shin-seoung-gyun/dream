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
		String host = "smtp.naver.com"; // 네이버일 경우 네이버 계정, gmail경우 gmail 계정 
		String user = "tlstmdrbsdustmq@naver.com"; // 패스워드 
		String password = "dustmqdydapdlf";
		
		// SMTP 서버 정보를 설정한다. 
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
			
			InternetAddress[] addArray = new InternetAddress[2]; //다인용
			addArray[0] = new InternetAddress("tlstmdrbsdustmq@naver.com"); 
			addArray[1] = new InternetAddress("sg0220.shin@daum.net"); 
	
			message.addRecipients(Message.RecipientType.TO, addArray);
			//message.addRecipient(Message.RecipientType.TO, new InternetAddress("seolmuah@naver.com"));//1인용
			
			// 메일 제목
			message.setSubject("테스트 메일입니다."); 
			// 메일 내용
			message.setText("빅데이터 분석 과정입니다."); 
			// send the message 
			Transport.send(message); 
			System.out.println("Success Message Send");

		} catch (MessagingException e) { 
			e.printStackTrace(); 
		}

	}

}
