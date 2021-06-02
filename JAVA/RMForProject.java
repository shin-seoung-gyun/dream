import java.text.SimpleDateFormat;

import javax.mail.Message;

public class RMForProject {
	String host = "imap.naver.com"; // imap 호스트 주소. ex) imap.gmail.com
	String userEmail = "tlstmdrbsdustmq@naver.com"; // 유저 이메일 주소
	String password = "dustmqdydapdlf"; // 유저 암호
	IMAPMailService mailService = new IMAPMailService();

	public void reciveMail() throws Exception {//
		DBAccess da = new DBAccess();
		mailService.login(host, userEmail, password);
		int messageCount = mailService.getMessageCount();
		// 테스트 목적이라서 5개 초과이면 5개만 처리: TODO 삭제
		if (messageCount > 10) {
			messageCount = 10;
		}
		Message[] msgArray = mailService.getMessages(true);
		for (int i = 0; i < messageCount; i++) {
			Message msg = msgArray[i];
			
			if (msg.getSubject() != null) {
				System.out.println("-------------------------------------------------------");
				// System.out.println(String.format("컨텐츠타임: %s", msg.getContentType()));
				SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
				String sendor = msg.getFrom()[0].toString();
				int lastIdx = (sendor.indexOf("<") == -1) ? sendor.length() : sendor.length() - 1;
				sendor = sendor.substring(sendor.indexOf("<") + 1, lastIdx);
				System.out.println(String.format("발신자: %s", sendor));
				// 발신자(이메일주소)로 이름 소속 부서 를 받아오는 함수 필요
				String[] strAry = da.findEMail2(sendor);
				System.out.println(String.format("발신자 이름: %s", strAry[0]));
				System.out.println(String.format("발신자 소속: %s", strAry[1]));
				System.out.println(String.format("발신자 부서: %s", strAry[2]));
				System.out.println(String.format("메일제목: %s", msg.getSubject()));
				System.out.println(String.format("메일발송시간: %s", format.format(msg.getSentDate())));
				System.out.println("읽은메일 :" + msg.getFlags());
				// 이름 소속 부서 추가해야함.
//	                 String mailText = mailService.getEmalText(msg.getContent());
//	                 System.out.println(String.format("메일내용: %s", mailText));
			}
		}
		mailService.logout(); // 로그아웃
	}

	public void reciveAllMail() throws Exception {// try구문을 사용하지않아서 필요한건가?
		DBAccess da = new DBAccess();
		mailService.login(host, userEmail, password);
		int messageCount = mailService.getMessageCount();
		// 테스트 목적이라서 5개 초과이면 5개만 처리: TODO 삭제
		if (messageCount > 10) {
			messageCount = 10;
		}
		Message[] msgArray = mailService.getMessages(false);
		for (int i = 0; i <messageCount; i++) {
			Message msg = msgArray[i];
			
			if (msg.getSubject() != null) {
				System.out.println("-------------------------------------------------------");
				// System.out.println(String.format("컨텐츠타임: %s", msg.getContentType()));
				SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
				String sendor = msg.getFrom()[0].toString();
				int lastIdx = (sendor.indexOf("<") == -1) ? sendor.length() : sendor.length() - 1;
				sendor = sendor.substring(sendor.indexOf("<") + 1, lastIdx);
				System.out.println(String.format("발신자: %s", sendor));
				// 발신자(이메일주소)로 이름 소속 부서 를 받아오는 함수 필요
				String[] strAry = da.findEMail2(sendor);
				System.out.println(String.format("발신자 이름: %s", strAry[0]));
				System.out.println(String.format("발신자 소속: %s", strAry[1]));
				System.out.println(String.format("발신자 부서: %s", strAry[2]));
				System.out.println(String.format("메일제목: %s", msg.getSubject()));
				System.out.println(String.format("메일발송시간: %s", format.format(msg.getSentDate())));
				System.out.println("읽은메일 :" + msg.getFlags());
				// 이름 소속 부서 추가해야함.
//	                 String mailText = mailService.getEmalText(msg.getContent());
//	                 System.out.println(String.format("메일내용: %s", mailText));
			}
		}
		mailService.logout(); // 로그아웃
	}

}
