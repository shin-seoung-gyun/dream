package model;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public interface DAO {
	//1.DB연결 (리턴 Connection 클래스)
	public Connection getConnection();
	//2.DB해제 (리턴 void)
	public void closeDBResources(ResultSet rs, Statement stmt, Connection conn);
		
}
