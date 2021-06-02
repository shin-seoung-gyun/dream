package memo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class JdbcUtil {
	static Connection getConn() {
		Connection conn = null;

		try {
			Class.forName("org.mariadb.jdbc.Driver");// 드라이버 로딩
			conn = DriverManager.getConnection("jdbc:mariadb://localhost:3306/mitbigdata", "bigdata", "1234");
		} catch (Exception e) {
			e.printStackTrace();
		}
		return conn;
	}

	static void close(Connection conn) {
		if (conn != null) {
			try {
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}

	static void close(PreparedStatement pstmt) {
		if (pstmt != null) {
			try {
				pstmt.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}

	static void close(ResultSet result) {
		if (result != null) {
			try {
				result.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}

	}

}
