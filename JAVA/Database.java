import java.sql.Connection;
import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class Database {

	private Connection con = null;
	private PreparedStatement pstm = null;
	private ResultSet rs = null;

	private void dbConn() {
		con = DBConnection.getConnection();
	}

	private void dbClose() {// db닫는 함수
		try {
			if (rs != null) {
				rs.close();
			}
			if (pstm != null) {
				pstm.close();
			}
			if (con != null) {
				con.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static final String Q_SHOW_ALL = "SELECT * FROM STUDENT WHERE STU_NAME=?";

	public void selectAllFromName(String name) {

		dbConn();

		try {
			pstm = con.prepareStatement(Q_SHOW_ALL);
			pstm.setString(1, name);
			rs = pstm.executeQuery();// 출력이 있을때 받아올 결과값이 있을때
			System.out.println("학생번호\t  이름\t학과 학년  반 성별 신장 체중");
			while (rs.next()) {
				String stu_no = rs.getString(1);
				String stu_name = rs.getString(2);
				String stu_dept = rs.getString(3);
				String stu_grade = rs.getString(4);
				String stu_class = rs.getString(5);
				String stu_gender = rs.getString(6);
				String stu_height = rs.getString(7);
				String stu_weight = rs.getString(8);

				System.out.printf("%s %s\t%s  %s   %s  %s  %s %s", stu_no, stu_name, stu_dept, stu_grade,
						stu_class, stu_gender, stu_height, stu_weight);
				System.out.println();

			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();

	}

}
