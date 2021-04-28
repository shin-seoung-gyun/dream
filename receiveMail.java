import java.text.SimpleDateFormat;

import javax.mail.Message;

public class receiveMail {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		// TODO Auto-generated method stub
				System.out.println("-- IMAP Emal 가져오기: Start\n\n");
		        String host = "imap.naver.com"; //imap 호스트 주소. ex) imap.gmail.com
		        String userEmail = "tlstmdrbsdustmq@naver.com"; //유저 이메일 주소
		        String password = "dustmqdydapdlf"; //유저 암호
		        IMAPMailService mailService = new IMAPMailService();
		        mailService.login(host, userEmail, password);
		        int messageCount = mailService.getMessageCount();
		        //테스트 목적이라서 5개 초과이면 5개만 처리: TODO 삭제
		        if (messageCount > 5) {
		             //messageCount = 5;
		        }
		        Message[] msgArray = mailService.getMessages(false);
		        for (int i = 0; i < msgArray.length; i++) {
		             Message msg = msgArray[i];
		             if (msg.getSubject() != null) {
		            	 System.out.println("-------------------------------------------------------");
			             //System.out.println(String.format("컨텐츠타임: %s", msg.getContentType()));
		            	 SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
		            	 String sendor = msg.getFrom()[0].toString();
		            	 int lastIdx = (sendor.indexOf("<")==-1) ? sendor.length():sendor.length()-1;
		            	 sendor = sendor.substring(sendor.indexOf("<")+1, lastIdx);
		            	 System.out.printf("메일번호: %d\n", i);
			             System.out.println(String.format("발신자: %s", sendor));
			             System.out.println(String.format("메일제목: %s", msg.getSubject()));
			             System.out.println(String.format("메일발송시간: %s", format.format(msg.getSentDate())));
			             System.out.println("읽은메일 :" + msg.getFlags());
			             
//		                 String mailText = mailService.getEmalText(msg.getContent());
//		                 System.out.println(String.format("메일내용: %s", mailText));
		             }
		        }
		        mailService.logout(); //로그아웃
		        System.out.println("\n\n-- IMAP Emal 가져오기: 종료");
	}

}
