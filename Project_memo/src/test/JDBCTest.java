package test;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class JDBCTest {

	public static void main(String[] args) {
		//마리아 db 연결 테스트
		Connection conn=null;
		PreparedStatement pstmt=null;
		ResultSet result =null;
		try {
			Class.forName("org.mariadb.jdbc.Driver");//드라이버 로딩
			conn = DriverManager.getConnection("jdbc:mariadb://localhost:3306/mitbigdata","bigdata","1234");
			pstmt=conn.prepareStatement("select count(no) from memo_table");
			result=pstmt.executeQuery();
			result.next();//한행씩 불러온다
			System.out.println("전체글 개수 ="+result.getString("count(no)"));
			
			System.out.println("이상 무");
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if(result != null) {try {result.close();} catch (SQLException e) {
					e.printStackTrace();
				}}
			if(pstmt !=null) {try {	pstmt.close();} catch (SQLException e) {
					e.printStackTrace();
				}}
			if (conn!=null) {try {conn.close();} catch (SQLException e) {
					e.printStackTrace();
				}
			}
			
		}
		
	}

}
