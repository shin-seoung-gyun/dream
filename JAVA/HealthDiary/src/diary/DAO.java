package diary;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public interface DAO {
	//1.DB연결
	public Connection getConnection();
	//2.DB삭제
	public void closeDBResources(ResultSet rs, Statement stmt, Connection conn);
		
}
