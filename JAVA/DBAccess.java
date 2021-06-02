import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class DBAccess {
	
	

	
	public static final String FIND_MAILADDRESS_READ = "select * from addressbook where 이메일주소 = ?";
	public static final String ALL_ADDRESS_READ = "select * from addressbook";
	public static final String FIND_NAME_READ = "select * from addressbook where 이름 = ?";
	public static final String FIND_AFFILIATION_READ = "select * from addressbook where 소속 = ?";
	public static final String FIND_AFFDIV_READ = "select * from addressbook where 소속 = ? and 부서 = ?";
	public static final String FIND_SENDMAIL_READ = "select * from (SELECT * FROM SENDMAIL ORDER BY no desc) WHERE ROWNUM<=10";
	
	public static final String SEND_MAIL_UPDATE = "insert into sendmail values (SQ_NO.nextval,?,?,?,to_date(?,'yyyy-MM-dd HH:mi:ss'))";
	public static final String INSERT_AB_UPDATE = "insert into addressbook values (SQ_NO3.nextval,?,?,?,?,?,?)";

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

	public void allAddress() {// 모든 주소록 불러오는 함수
		dbConn();// DB접속
		try {

			pstm = con.prepareStatement(ALL_ADDRESS_READ);
			rs = pstm.executeQuery();
			System.out.println("번호 이름\t소속\t\t부서\t직급\t연락처\t\t이메일주소");
			while (rs.next()) {
				String no = rs.getString("no");
				System.out.print(no);
				String name = rs.getString("이름");
				System.out.print("  " + name);
				String affiliation = rs.getString("소속");
				System.out.print("\t" + affiliation);
				if (affiliation.length() < 5) {
					System.out.print("\t");
				}
				String divisions = rs.getString("부서");
				System.out.print("\t" + divisions);
				String position = rs.getString("직급");
				System.out.print("\t" + position);
				String phone = rs.getString("연락처");
				System.out.print("\t" + phone);
				String eMail = rs.getString("이메일주소");
				System.out.print("\t" + eMail);
				System.out.println();
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
	}
	
	public List<String> allAddAry() {// 모든 주소록 불러서 메일주소만 리스트로 리턴하는 함수
		dbConn();// DB접속
		List<String> result=new ArrayList<>();
		try {

			pstm = con.prepareStatement(ALL_ADDRESS_READ);
			rs = pstm.executeQuery();
			while (rs.next()) {
				String eMail = rs.getString("이메일주소");
				result.add(eMail);
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
		return result;
	}

	public void findNameAddress(String name1) {// 이름으로 주소록 찾는 함수
		dbConn();// DB접속

		try {
			pstm = con.prepareStatement(FIND_NAME_READ);
			pstm.setString(1, name1);
			rs = pstm.executeQuery();
			System.out.println("번호 이름\t소속\t\t부서\t직급\t연락처\t\t이메일주소");
			while (rs.next()) {
				String no = rs.getString("no");
				System.out.print(no);
				String name = rs.getString("이름");
				System.out.print("  " + name);
				String affiliation = rs.getString("소속");
				System.out.print("\t" + affiliation);
				if (affiliation.length() < 9) {
					System.out.print("\t");
				}
				String divisions = rs.getString("부서");
				System.out.print("\t" + divisions);
				String position = rs.getString("직급");
				System.out.print("\t" + position);
				String phone = rs.getString("연락처");
				System.out.print("\t" + phone);
				String eMail = rs.getString("이메일주소");
				System.out.print("\t" + eMail);
				System.out.println();
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
	}

	public void findAffiliationAddress(String affiliation1) {// 소속으로 주소록 찾는 함수
		dbConn();// DB접속

		try {
			pstm = con.prepareStatement(FIND_AFFILIATION_READ);
			pstm.setString(1, affiliation1);
			rs = pstm.executeQuery();
			System.out.println("번호 이름\t소속\t\t부서\t직급\t연락처\t\t이메일주소");
			while (rs.next()) {
				String no = rs.getString("no");
				System.out.print(no);
				String name = rs.getString("이름");
				System.out.print("  " + name);
				String affiliation = rs.getString("소속");
				System.out.print("\t" + affiliation);
				if (affiliation.length() < 9) {
					System.out.print("\t");
				}
				String divisions = rs.getString("부서");
				System.out.print("\t" + divisions);
				String position = rs.getString("직급");
				System.out.print("\t" + position);
				String phone = rs.getString("연락처");
				System.out.print("\t" + phone);
				String eMail = rs.getString("이메일주소");
				System.out.print("\t" + eMail);
				System.out.println();
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
	}
	
	public List<String> findAffAdd(String affiliation1) {// 소속으로 메일주소 가져오는 함수
		dbConn();// DB접속
		List<String> result=new ArrayList<>();
		try {
			pstm = con.prepareStatement(FIND_AFFILIATION_READ);
			pstm.setString(1, affiliation1);
			rs = pstm.executeQuery();
			
			while (rs.next()) {
				
				String eMail = rs.getString("이메일주소");
				result.add(eMail);
				
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
		return result;
	}
	
	public List<String> findAffDivAdd(String affiliation1,String divisions) {// 소속및 부서로 메일주소 가져오는 함수
		dbConn();// DB접속
		List<String> result=new ArrayList<>();
		try {
			pstm = con.prepareStatement(FIND_AFFDIV_READ);
			pstm.setString(1, affiliation1);
			pstm.setString(2, divisions);
			rs = pstm.executeQuery();
			
			while (rs.next()) {
				
				String eMail = rs.getString("이메일주소");
				result.add(eMail);
				
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
		return result;
	}

	public boolean isTure(String mailID) {
		boolean result = false;
		dbConn();// DB접속

		try {
			pstm = con.prepareStatement(FIND_MAILADDRESS_READ);
			pstm.setString(1, mailID);
			rs = pstm.executeQuery();
			while (rs.next()) {
				String no = rs.getString("no");
				if (no == null) {
					result = false;
				} else {
					result = true;
				}
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료

		return result;
	}

	private String[] findEMail(String mailID) {// 이메일로 주소록찾아서 이름과 직급 찾는 함수
		dbConn();// DB접속
		String[] reAry = new String[2];
		try {
			pstm = con.prepareStatement(FIND_MAILADDRESS_READ);
			pstm.setString(1, mailID);
			rs = pstm.executeQuery();

			while (rs.next()) {
				String name = rs.getString("이름");
				String position = rs.getString("직급");
				reAry[0] = name;
				reAry[1] = position;
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
		return reAry;
	}
	
	public String[] findEMail2(String mailID) {// 이메일로 주소록찾아서 이름과 직급 부서 찾는 함수
		dbConn();// DB접속
		String[] reAry = new String[3];
		try {
			pstm = con.prepareStatement(FIND_MAILADDRESS_READ);
			pstm.setString(1, mailID);
			rs = pstm.executeQuery();

			while (rs.next()) {
				String name = rs.getString("이름");
				String position = rs.getString("소속");
				String divisions = rs.getString("부서");
				reAry[0] = name;
				reAry[1] = position;
				reAry[2] = divisions;
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
		return reAry;
	}

	
	
	public String baseText(String mainText, String mailID) {// 주소에 있는 대상일경우 기본으로 출력할 텍스트

		var Ary = findEMail(mailID);
		String rename = Ary[0];
		String reposition = Ary[1];
		String result = String.format("안녕하세요. %s%s님\n무소속 신승균 입니다.\n", rename, reposition) + mainText
				+ "\n감사합니다.\n무소속 무부서 학생 신승균(010-4923-2964)";
		return result;
	}
	
	
	public void sendMail(String mailID, String title, String mainText,String date) {//보낸 메일 데이터베이스에 저장
		dbConn();// DB접속
		try {
			pstm = con.prepareStatement(SEND_MAIL_UPDATE);
			pstm.setString(1, mailID);
			pstm.setString(2, title);
			pstm.setString(3, mainText);
			pstm.setString(4, date);
			pstm.executeUpdate();
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
		
		
	}
	
	public void findSendMail() {//보낸 메일 보기 - 최근 최대 10건 (받은사람 이메일, 타이틀, 보낸날짜)
		dbConn();// DB접속
		try {
			pstm = con.prepareStatement(FIND_SENDMAIL_READ);
			rs = pstm.executeQuery();
			System.out.println("받는사람이메일주소\t\t\t타이틀\t\t\t보낸날짜");
			while (rs.next()) {
				String eMail = rs.getString("받는사람이메일주소");
				System.out.print(eMail);
				if(eMail.length()<21) {
					System.out.print("\t");
				}
				String title = rs.getString("타이틀");
				System.out.print("\t"+title);
				if(title.length()<5) {
					System.out.print("\t\t");
				}
				String date = rs.getString("보낸날짜");
				System.out.print("\t"+date+"\n");
			
			}
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
		
	}
	
	
	public void insertAB(String name, String divisions, String position,String phone,String eMail,String affiliation) {//주소록 추가하는 함수
		dbConn();// DB접속
		try {
			pstm = con.prepareStatement(INSERT_AB_UPDATE);
			pstm.setString(1, name);
			pstm.setString(2, divisions);
			pstm.setString(3, position);
			pstm.setString(4, phone);
			pstm.setString(5, eMail);
			pstm.setString(6, affiliation);
			pstm.executeUpdate();
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
	}
	
	public void setColumn(int no, String column, String text) {//칼럼명을 입력받아 수정
		
		String UPDATE_ADDRESS_BOOK = "update addressbook set " + column +"=? Where no=?";//꼭 상수를 사용할 필요는 없음
	
		dbConn();// DB접속
		try {
			pstm = con.prepareStatement(UPDATE_ADDRESS_BOOK);
			
			pstm.setString(1, text);
			pstm.setInt(2, no);
			pstm.executeUpdate();
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
	}
	
public void deleteDate(int no) {//칼럼명을 입력받아 수정
		
		String DELETE_ADDRESS_DATE = "DELETE FROM addressbook Where no=?";
	
		dbConn();// DB접속
		try {
			pstm = con.prepareStatement(DELETE_ADDRESS_DATE);
			pstm.setInt(1, no);
			pstm.executeUpdate();
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB접속종료
	}
	
	
	
	
	
	
	
	
	

}
