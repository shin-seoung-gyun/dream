
import java.sql.Connection;
import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class DBAccess {

	public class DBItem {
		public String item;
		public String money;
		public Date date1;

		public DBItem(String item, String money, Date date1) {
			this.item = (item == null) ? "" : item;
			this.money = (money == null) ? "" : money;
			this.date1 = date1;
		}

		public DBItem(String item, String money) {
			this.item = (item == null) ? "" : item;
			this.money = (money == null) ? "" : money;

		}
		public DBItem(String item, Date date1) {
			this.item = (item == null) ? "" : item;
			this.date1 = date1;

		}
	}
	private static final String Q_SHOW_LISTDAILYMONEY = "select money as �������� , inoutdate as ���� "
			+ "from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd')";

	private static final String Q_SHOW_LISTDAILY = "select DISTINCT " + "(select sum(money) from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd') AND money>0) as ����, "
			+ "(select sum(money) from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd') AND money<0) as ���� "
			+ "from pocketmoney";
	
	private static final String Q_SHOW_LISTDAILYAVG =  "select DISTINCT " + "(select avg(money) from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd') AND money>0) as �������, "
			+ "(select avg(money) from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd') AND money<0) as ������� "
			+ "from pocketmoney";

	private static final String Q_SELECT_OUTRANK = "SELECT item,p1 FROM (SELECT item,SUM(MONEY) "
			+ "as p1 FROM pocketmoney WHERE (MONEY<0)GROUP BY ITEM ORDER BY SUM(MONEY))" + " Where Rownum<=3";// �����
																												// 1~3��
																												// ���
	private static final String Q_DELETE_LASTITEM = "Delete from pocketmoney " + "where no in (select max(no) "
			+ "from pocketmoney)";// ������
									// �Է�
									// ���
	private static final String Q_SHOW_ALLITEM = "SELECT ITEM,MONEY,inoutdate FROM POCKETMONEY ORDER BY NO DESC";
	private static final String Q_SHOW_MONEY = "SELECT SUM(MONEY) AS BAL FROM POCKETMONEY";
	private static final String Q_INSERT_ITEM = "INSERT INTO POCKETMONEY VALUES(SEQ_PM.NEXTVAL,?,?,?)";

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

	public void insertRow(String item, String money, String date) {// �Է��ϴ� �ż���
		dbConn();
		try {
			pstm = con.prepareStatement(Q_INSERT_ITEM);
			pstm.setString(1, item);
			pstm.setInt(2, Integer.parseInt(money));
			pstm.setString(3, date);
			pstm.executeUpdate();// ��¾��� ������Ʈ���Ҷ�
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();

	}

	public int getMoneyBalance() {// �ܾ�
		dbConn();
		try {
			pstm = con.prepareStatement(Q_SHOW_MONEY);
			rs = pstm.executeQuery();// ����� ������ �޾ƿ� ������� ������
			if (rs.next()) {
				return rs.getInt("bal");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
		return 0;
	}

	public List<DBItem> selectAllItem() {

		dbConn();
		List<DBItem> listItem = new ArrayList<>();
		try {
			pstm = con.prepareStatement(Q_SHOW_ALLITEM);
			rs = pstm.executeQuery();// ����� ������ �޾ƿ� ������� ������
			while (rs.next()) {
				listItem.add(new DBItem(rs.getString("item"), rs.getString("money"), rs.getDate("inoutdate")));// ����Ʈ��
																												// Ŭ����������
																												// �ִ°�
																												// ������ ��
																												// ����
																												// Ÿ����
				// �������� ���� �����Ƿ�
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
		return listItem;
	}

	public void lastOrderCancle() {// �������Է� ���
		dbConn();
		try {
			pstm = con.prepareStatement(Q_DELETE_LASTITEM);// ���๮�� ��񿡼� �����ϴ� ó��
			pstm.executeUpdate();// ��¾��� ������Ʈ���Ҷ�
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
	}

	public List<DBItem> outPocket() {// ����� 1~3�� ���
		dbConn();
		List<DBItem> rankItem = new ArrayList<>();
		try {

			pstm = con.prepareStatement(Q_SELECT_OUTRANK);
			rs = pstm.executeQuery();// ����� ������ �޾ƿ� ������� ������
			while (rs.next()) {
				rankItem.add(new DBItem(rs.getString("item"), rs.getString("p1")));// ����Ʈ�� Ŭ���������� �ִ°� ������ �� ���� Ÿ���� ��������
																					// ���� �����Ƿ�
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
		return rankItem;
	}

	public List<DBItem> dailyInOut(String startDate, String endDate) {

		dbConn();
		List<DBItem> listDaily = new ArrayList<>();
		try {
			pstm = con.prepareStatement(Q_SHOW_LISTDAILY);

			pstm.setString(1, startDate);// ���� ��
			pstm.setString(2, endDate);// ����
			pstm.setString(3, startDate);// ���۳�
			pstm.setString(4, endDate);// ����
			rs = pstm.executeQuery();// ����� ������ �޾ƿ� ������� ������
			while (rs.next()) {
				listDaily.add(new DBItem(rs.getString("����"), rs.getString("����")));// ����Ʈ�� Ŭ���������� �ִ°� ������ �� ���� Ÿ����
																					// �������� ���� �����Ƿ�
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
		return listDaily;
	}
	
	public List<DBItem> dailyInOutAvg(String startDate, String endDate) {

		dbConn();
		List<DBItem> listDailyAvg = new ArrayList<>();
		try {
			pstm = con.prepareStatement(Q_SHOW_LISTDAILYAVG);

			pstm.setString(1, startDate);// ���� ��
			pstm.setString(2, endDate);// ����
			pstm.setString(3, startDate);// ���۳�
			pstm.setString(4, endDate);// ����
			rs = pstm.executeQuery();// ����� ������ �޾ƿ� ������� ������
			while (rs.next()) {
				listDailyAvg.add(new DBItem(rs.getString("�������"), rs.getString("�������")));// ����Ʈ�� Ŭ���������� �ִ°� ������ �� ���� Ÿ����
																					// �������� ���� �����Ƿ�
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
		return listDailyAvg;
	}
	
	public List<DBItem> dailyInOutMoney(String startDate, String endDate) {

		dbConn();
		List<DBItem> listDailyMoney = new ArrayList<>();
		try {
			pstm = con.prepareStatement(Q_SHOW_LISTDAILYMONEY);

			pstm.setString(1, startDate);// ���� ��
			pstm.setString(2, endDate);// ����
			rs = pstm.executeQuery();// ����� ������ �޾ƿ� ������� ������
			while (rs.next()) {
				listDailyMoney.add(new DBItem(rs.getString("��������"), rs.getDate("����")));// ����Ʈ�� Ŭ���������� �ִ°� ������ �� ���� Ÿ����
																					// �������� ���� �����Ƿ�
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
		return listDailyMoney;
	}

}
