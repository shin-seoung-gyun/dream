package test;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class JDBCTest {

	public static void main(String[] args) {
		//������ db ���� �׽�Ʈ
		Connection conn=null;
		PreparedStatement pstmt=null;
		ResultSet result =null;
		try {
			Class.forName("org.mariadb.jdbc.Driver");//����̹� �ε�
			conn = DriverManager.getConnection("jdbc:mariadb://localhost:3306/mitbigdata","bigdata","1234");
			pstmt=conn.prepareStatement("select count(no) from memo_table");
			result=pstmt.executeQuery();
			result.next();//���྿ �ҷ��´�
			System.out.println("��ü�� ���� ="+result.getString("count(no)"));
			
			System.out.println("�̻� ��");
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
