
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
 
public class DBConnection 
{
    public static Connection dbConn;
    
        public static Connection getConnection()
        {
            Connection conn = null;
            try {
                String user = "shinseounggyun"; 
                String pw = "1234";
                String url = "jdbc:oracle:thin:@localhost:1521:XE";
                
                Class.forName("oracle.jdbc.driver.OracleDriver");        
                conn = DriverManager.getConnection(url, user, pw);
                
            } catch (ClassNotFoundException cnfe) {
                System.out.println("DB ����̹� �ε� ���� :"+cnfe.toString());
            } catch (SQLException sqle) {
                System.out.println("DB ���ӽ��� : "+sqle.toString());
            } catch (Exception e) {
                System.out.println("Unkonwn error");
                e.printStackTrace();
            }
            return conn;     
        }
}
 

