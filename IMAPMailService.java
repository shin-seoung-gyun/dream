import java.util.Properties;

import javax.mail.Flags;
import javax.mail.Folder;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Multipart;
import javax.mail.Session;
import javax.mail.Store;
import javax.mail.URLName;
import javax.mail.search.FlagTerm;

public class IMAPMailService {
	private Session session;
    private Store store;
    private Folder folder;
    // hardcoding protocol and the folder
    // it can be parameterized and enhanced as required
    private String protocol = "imaps";
    private String file = "INBOX";
    public IMAPMailService() {
    }
    public boolean isLoggedIn() {
         return store.isConnected();
    }
    /**
     * 메일 본문 텍스트 내용을 가져옴
     *
     * @param content
     * @return
     * @throws Exception
     */
    public String getEmalText(Object content) throws Exception {
         //TODO: 개발 필요
         System.out.println("####  컨텐츠 타입에 따라서 text body 또는 멀티파트 처리 기능 구현이 필요");
         if (content instanceof Multipart) {
              System.out.println("Multipart 이메일임");
         } else {
              System.out.println(content);
         }
         return null;
    }
    /**
     * to login to the mail host server
     */
    public void login(String host, String username, String password) throws Exception {
         URLName url = new URLName(protocol, host, 993, file, username, password);
         if (session == null) {
              Properties props = null;
              try {
                   props = System.getProperties();
              } catch (SecurityException sex) {
                   props = new Properties();
              }
              session = Session.getInstance(props, null);
         }
         store = session.getStore(url);
         store.connect();
         folder = store.getFolder("inbox"); //inbox는 받은 메일함을 의미
         //folder.open(Folder.READ_WRITE);
         folder.open(Folder.READ_ONLY); //읽기 전용
    }
    /**
     * to logout from the mail host server
     */
    public void logout() throws MessagingException {
         folder.close(false);
         store.close();
         store = null;
         session = null;
    }
    public int getMessageCount() {
         //TODO: 안 읽은 메일의 건수만 조회하는 기능 추가
         int messageCount = 0;
         try {
              messageCount = folder.getMessageCount();
         } catch (MessagingException me) {
              me.printStackTrace();
         }
         return messageCount;
    }
    /**
     * 이메일 리스트를 가져옴
     *
     * @param onlyNotRead 안읽은 메일 리스트만 가져올지 여부
     * @return
     * @throws MessagingException
     */
    public Message[] getMessages(boolean onlyNotRead) throws MessagingException {
         if (onlyNotRead) {
              return folder.search(new FlagTerm(new Flags(Flags.Flag.SEEN), false));
         } else {
              return folder.getMessages();
         }
    }


}
