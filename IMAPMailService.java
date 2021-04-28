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
     * ���� ���� �ؽ�Ʈ ������ ������
     *
     * @param content
     * @return
     * @throws Exception
     */
    public String getEmalText(Object content) throws Exception {
         //TODO: ���� �ʿ�
         System.out.println("####  ������ Ÿ�Կ� ���� text body �Ǵ� ��Ƽ��Ʈ ó�� ��� ������ �ʿ�");
         if (content instanceof Multipart) {
              System.out.println("Multipart �̸�����");
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
         folder = store.getFolder("inbox"); //inbox�� ���� �������� �ǹ�
         //folder.open(Folder.READ_WRITE);
         folder.open(Folder.READ_ONLY); //�б� ����
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
         //TODO: �� ���� ������ �Ǽ��� ��ȸ�ϴ� ��� �߰�
         int messageCount = 0;
         try {
              messageCount = folder.getMessageCount();
         } catch (MessagingException me) {
              me.printStackTrace();
         }
         return messageCount;
    }
    /**
     * �̸��� ����Ʈ�� ������
     *
     * @param onlyNotRead ������ ���� ����Ʈ�� �������� ����
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
