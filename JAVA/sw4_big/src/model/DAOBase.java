
package model;

import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.SQLException;

public class DAOBase implements DAO {
	public Connection getConnection(){
		String jdbc_driver = "org.mariadb.jdbc.Driver";
		String db_url = "jdbc:mariadb://localhost:3306/sampledb";
		try {
			Class.forName(jdbc_driver);
			Connection conn = DriverManager.getConnection(db_url, "hrd", "hrdkorea");
			System.out.println("종료");
			return conn;
		} catch (Exception e) {
			e.printStackTrace();
		}
		return null;
	}

	public void closeDBResources(ResultSet rs, Statement stmt, Connection conn) {
		if (rs != null) {
			try {
				System.out.println("rs 종료");
				rs.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		if (stmt != null) {
			try {
				System.out.println("stmt 종료");
				stmt.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		if (conn != null) {
			try {
				System.out.println("conn 종료");
				conn.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
}
