import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class DBAccess {
	
	

	
	public static final String FIND_MAILADDRESS_READ = "select * from addressbook where �̸����ּ� = ?";
	public static final String ALL_ADDRESS_READ = "select * from addressbook";
	public static final String FIND_NAME_READ = "select * from addressbook where �̸� = ?";
	public static final String FIND_AFFILIATION_READ = "select * from addressbook where �Ҽ� = ?";
	public static final String FIND_AFFDIV_READ = "select * from addressbook where �Ҽ� = ? and �μ� = ?";
	public static final String FIND_SENDMAIL_READ = "select * from (SELECT * FROM SENDMAIL ORDER BY no desc) WHERE ROWNUM<=10";
	
	public static final String SEND_MAIL_UPDATE = "insert into sendmail values (SQ_NO.nextval,?,?,?,to_date(?,'yyyy-MM-dd HH:mi:ss'))";
	public static final String INSERT_AB_UPDATE = "insert into addressbook values (SQ_NO3.nextval,?,?,?,?,?,?)";

	private Connection con = null;
	private PreparedStatement pstm = null;
	private ResultSet rs = null;

	private void dbConn() {
		con = DBConnection.getConnection();
	}

	private void dbClose() {// db�ݴ� �Լ�
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

	public void allAddress() {// ��� �ּҷ� �ҷ����� �Լ�
		dbConn();// DB����
		try {

			pstm = con.prepareStatement(ALL_ADDRESS_READ);
			rs = pstm.executeQuery();
			System.out.println("��ȣ �̸�\t�Ҽ�\t\t�μ�\t����\t����ó\t\t�̸����ּ�");
			while (rs.next()) {
				String no = rs.getString("no");
				System.out.print(no);
				String name = rs.getString("�̸�");
				System.out.print("  " + name);
				String affiliation = rs.getString("�Ҽ�");
				System.out.print("\t" + affiliation);
				if (affiliation.length() < 5) {
					System.out.print("\t");
				}
				String divisions = rs.getString("�μ�");
				System.out.print("\t" + divisions);
				String position = rs.getString("����");
				System.out.print("\t" + position);
				String phone = rs.getString("����ó");
				System.out.print("\t" + phone);
				String eMail = rs.getString("�̸����ּ�");
				System.out.print("\t" + eMail);
				System.out.println();
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
	}
	
	public List<String> allAddAry() {// ��� �ּҷ� �ҷ��� �����ּҸ� ����Ʈ�� �����ϴ� �Լ�
		dbConn();// DB����
		List<String> result=new ArrayList<>();
		try {

			pstm = con.prepareStatement(ALL_ADDRESS_READ);
			rs = pstm.executeQuery();
			while (rs.next()) {
				String eMail = rs.getString("�̸����ּ�");
				result.add(eMail);
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
		return result;
	}

	public void findNameAddress(String name1) {// �̸����� �ּҷ� ã�� �Լ�
		dbConn();// DB����

		try {
			pstm = con.prepareStatement(FIND_NAME_READ);
			pstm.setString(1, name1);
			rs = pstm.executeQuery();
			System.out.println("��ȣ �̸�\t�Ҽ�\t\t�μ�\t����\t����ó\t\t�̸����ּ�");
			while (rs.next()) {
				String no = rs.getString("no");
				System.out.print(no);
				String name = rs.getString("�̸�");
				System.out.print("  " + name);
				String affiliation = rs.getString("�Ҽ�");
				System.out.print("\t" + affiliation);
				if (affiliation.length() < 9) {
					System.out.print("\t");
				}
				String divisions = rs.getString("�μ�");
				System.out.print("\t" + divisions);
				String position = rs.getString("����");
				System.out.print("\t" + position);
				String phone = rs.getString("����ó");
				System.out.print("\t" + phone);
				String eMail = rs.getString("�̸����ּ�");
				System.out.print("\t" + eMail);
				System.out.println();
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
	}

	public void findAffiliationAddress(String affiliation1) {// �Ҽ����� �ּҷ� ã�� �Լ�
		dbConn();// DB����

		try {
			pstm = con.prepareStatement(FIND_AFFILIATION_READ);
			pstm.setString(1, affiliation1);
			rs = pstm.executeQuery();
			System.out.println("��ȣ �̸�\t�Ҽ�\t\t�μ�\t����\t����ó\t\t�̸����ּ�");
			while (rs.next()) {
				String no = rs.getString("no");
				System.out.print(no);
				String name = rs.getString("�̸�");
				System.out.print("  " + name);
				String affiliation = rs.getString("�Ҽ�");
				System.out.print("\t" + affiliation);
				if (affiliation.length() < 9) {
					System.out.print("\t");
				}
				String divisions = rs.getString("�μ�");
				System.out.print("\t" + divisions);
				String position = rs.getString("����");
				System.out.print("\t" + position);
				String phone = rs.getString("����ó");
				System.out.print("\t" + phone);
				String eMail = rs.getString("�̸����ּ�");
				System.out.print("\t" + eMail);
				System.out.println();
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
	}
	
	public List<String> findAffAdd(String affiliation1) {// �Ҽ����� �����ּ� �������� �Լ�
		dbConn();// DB����
		List<String> result=new ArrayList<>();
		try {
			pstm = con.prepareStatement(FIND_AFFILIATION_READ);
			pstm.setString(1, affiliation1);
			rs = pstm.executeQuery();
			
			while (rs.next()) {
				
				String eMail = rs.getString("�̸����ּ�");
				result.add(eMail);
				
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
		return result;
	}
	
	public List<String> findAffDivAdd(String affiliation1,String divisions) {// �Ҽӹ� �μ��� �����ּ� �������� �Լ�
		dbConn();// DB����
		List<String> result=new ArrayList<>();
		try {
			pstm = con.prepareStatement(FIND_AFFDIV_READ);
			pstm.setString(1, affiliation1);
			pstm.setString(2, divisions);
			rs = pstm.executeQuery();
			
			while (rs.next()) {
				
				String eMail = rs.getString("�̸����ּ�");
				result.add(eMail);
				
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
		return result;
	}

	public boolean isTure(String mailID) {
		boolean result = false;
		dbConn();// DB����

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
		dbClose();// DB��������

		return result;
	}

	private String[] findEMail(String mailID) {// �̸��Ϸ� �ּҷ�ã�Ƽ� �̸��� ���� ã�� �Լ�
		dbConn();// DB����
		String[] reAry = new String[2];
		try {
			pstm = con.prepareStatement(FIND_MAILADDRESS_READ);
			pstm.setString(1, mailID);
			rs = pstm.executeQuery();

			while (rs.next()) {
				String name = rs.getString("�̸�");
				String position = rs.getString("����");
				reAry[0] = name;
				reAry[1] = position;
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
		return reAry;
	}
	
	public String[] findEMail2(String mailID) {// �̸��Ϸ� �ּҷ�ã�Ƽ� �̸��� ���� �μ� ã�� �Լ�
		dbConn();// DB����
		String[] reAry = new String[3];
		try {
			pstm = con.prepareStatement(FIND_MAILADDRESS_READ);
			pstm.setString(1, mailID);
			rs = pstm.executeQuery();

			while (rs.next()) {
				String name = rs.getString("�̸�");
				String position = rs.getString("�Ҽ�");
				String divisions = rs.getString("�μ�");
				reAry[0] = name;
				reAry[1] = position;
				reAry[2] = divisions;
			}

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
		return reAry;
	}

	
	
	public String baseText(String mainText, String mailID) {// �ּҿ� �ִ� ����ϰ�� �⺻���� ����� �ؽ�Ʈ

		var Ary = findEMail(mailID);
		String rename = Ary[0];
		String reposition = Ary[1];
		String result = String.format("�ȳ��ϼ���. %s%s��\n���Ҽ� �Ž±� �Դϴ�.\n", rename, reposition) + mainText
				+ "\n�����մϴ�.\n���Ҽ� ���μ� �л� �Ž±�(010-4923-2964)";
		return result;
	}
	
	
	public void sendMail(String mailID, String title, String mainText,String date) {//���� ���� �����ͺ��̽��� ����
		dbConn();// DB����
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
		dbClose();// DB��������
		
		
	}
	
	public void findSendMail() {//���� ���� ���� - �ֱ� �ִ� 10�� (������� �̸���, Ÿ��Ʋ, ������¥)
		dbConn();// DB����
		try {
			pstm = con.prepareStatement(FIND_SENDMAIL_READ);
			rs = pstm.executeQuery();
			System.out.println("�޴»���̸����ּ�\t\t\tŸ��Ʋ\t\t\t������¥");
			while (rs.next()) {
				String eMail = rs.getString("�޴»���̸����ּ�");
				System.out.print(eMail);
				if(eMail.length()<21) {
					System.out.print("\t");
				}
				String title = rs.getString("Ÿ��Ʋ");
				System.out.print("\t"+title);
				if(title.length()<5) {
					System.out.print("\t\t");
				}
				String date = rs.getString("������¥");
				System.out.print("\t"+date+"\n");
			
			}
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
		
	}
	
	
	public void insertAB(String name, String divisions, String position,String phone,String eMail,String affiliation) {//�ּҷ� �߰��ϴ� �Լ�
		dbConn();// DB����
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
		dbClose();// DB��������
	}
	
	public void setColumn(int no, String column, String text) {//Į������ �Է¹޾� ����
		
		String UPDATE_ADDRESS_BOOK = "update addressbook set " + column +"=? Where no=?";//�� ����� ����� �ʿ�� ����
	
		dbConn();// DB����
		try {
			pstm = con.prepareStatement(UPDATE_ADDRESS_BOOK);
			
			pstm.setString(1, text);
			pstm.setInt(2, no);
			pstm.executeUpdate();
			
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
	}
	
public void deleteDate(int no) {//Į������ �Է¹޾� ����
		
		String DELETE_ADDRESS_DATE = "DELETE FROM addressbook Where no=?";
	
		dbConn();// DB����
		try {
			pstm = con.prepareStatement(DELETE_ADDRESS_DATE);
			pstm.setInt(1, no);
			pstm.executeUpdate();
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		dbClose();// DB��������
	}
	
	
	
	
	
	
	
	
	

}
