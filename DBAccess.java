
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
	private static final String Q_SHOW_LISTDAILYMONEY = "select money as 수입지출 , inoutdate as 일자 "
			+ "from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd')";

	private static final String Q_SHOW_LISTDAILY = "select DISTINCT " + "(select sum(money) from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd') AND money>0) as 수입, "
			+ "(select sum(money) from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd') AND money<0) as 지출 "
			+ "from pocketmoney";
	
	private static final String Q_SHOW_LISTDAILYAVG =  "select DISTINCT " + "(select avg(money) from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd') AND money>0) as 수입평균, "
			+ "(select avg(money) from pocketmoney "
			+ "where inoutdate BETWEEN TO_DATE(?, 'yyyy-mm-dd') and TO_DATE(?, 'yyyy-mm-dd') AND money<0) as 지출평균 "
			+ "from pocketmoney";

	private static final String Q_SELECT_OUTRANK = "SELECT item,p1 FROM (SELECT item,SUM(MONEY) "
			+ "as p1 FROM pocketmoney WHERE (MONEY<0)GROUP BY ITEM ORDER BY SUM(MONEY))" + " Where Rownum<=3";// 지출액
																												// 1~3위
																												// 출력
	private static final String Q_DELETE_LASTITEM = "Delete from pocketmoney " + "where no in (select max(no) "
			+ "from pocketmoney)";// 마지막
									// 입력
									// 취소
	private static final String Q_SHOW_ALLITEM = "SELECT ITEM,MONEY,inoutdate FROM POCKETMONEY ORDER BY NO DESC";
	private static final String Q_SHOW_MONEY = "SELECT SUM(MONEY) AS BAL FROM POCKETMONEY";
	private static final String Q_INSERT_ITEM = "INSERT INTO POCKETMONEY VALUES(SEQ_PM.NEXTVAL,?,?,?)";

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

	public void insertRow(String item, String money, String date) {// 입력하는 매서드
		dbConn();
		try {
			pstm = con.prepareStatement(Q_INSERT_ITEM);
			pstm.setString(1, item);
			pstm.setInt(2, Integer.parseInt(money));
			pstm.setString(3, date);
			pstm.executeUpdate();// 출력없이 업데이트만할때
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();

	}

	public int getMoneyBalance() {// 잔액
		dbConn();
		try {
			pstm = con.prepareStatement(Q_SHOW_MONEY);
			rs = pstm.executeQuery();// 출력이 있을때 받아올 결과값이 있을때
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
			rs = pstm.executeQuery();// 출력이 있을때 받아올 결과값이 있을때
			while (rs.next()) {
				listItem.add(new DBItem(rs.getString("item"), rs.getString("money"), rs.getDate("inoutdate")));// 리스트에
																												// 클래스단위로
																												// 넣는게
																												// 구조상 더
																												// 좋음
																												// 타입이
				// 여러개가 들어갈수 있으므로
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
		return listItem;
	}

	public void lastOrderCancle() {// 마지막입력 취소
		dbConn();
		try {
			pstm = con.prepareStatement(Q_DELETE_LASTITEM);// 실행문을 디비에서 실행하는 처리
			pstm.executeUpdate();// 출력없이 업데이트만할때
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
	}

	public List<DBItem> outPocket() {// 지출액 1~3위 출력
		dbConn();
		List<DBItem> rankItem = new ArrayList<>();
		try {

			pstm = con.prepareStatement(Q_SELECT_OUTRANK);
			rs = pstm.executeQuery();// 출력이 있을때 받아올 결과값이 있을때
			while (rs.next()) {
				rankItem.add(new DBItem(rs.getString("item"), rs.getString("p1")));// 리스트에 클래스단위로 넣는게 구조상 더 좋음 타입이 여러개가
																					// 들어갈수 있으므로
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

			pstm.setString(1, startDate);// 시작 날
			pstm.setString(2, endDate);// 끝날
			pstm.setString(3, startDate);// 시작날
			pstm.setString(4, endDate);// 끝날
			rs = pstm.executeQuery();// 출력이 있을때 받아올 결과값이 있을때
			while (rs.next()) {
				listDaily.add(new DBItem(rs.getString("수입"), rs.getString("지출")));// 리스트에 클래스단위로 넣는게 구조상 더 좋음 타입이
																					// 여러개가 들어갈수 있으므로
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

			pstm.setString(1, startDate);// 시작 날
			pstm.setString(2, endDate);// 끝날
			pstm.setString(3, startDate);// 시작날
			pstm.setString(4, endDate);// 끝날
			rs = pstm.executeQuery();// 출력이 있을때 받아올 결과값이 있을때
			while (rs.next()) {
				listDailyAvg.add(new DBItem(rs.getString("수입평균"), rs.getString("지출평균")));// 리스트에 클래스단위로 넣는게 구조상 더 좋음 타입이
																					// 여러개가 들어갈수 있으므로
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

			pstm.setString(1, startDate);// 시작 날
			pstm.setString(2, endDate);// 끝날
			rs = pstm.executeQuery();// 출력이 있을때 받아올 결과값이 있을때
			while (rs.next()) {
				listDailyMoney.add(new DBItem(rs.getString("수입지출"), rs.getDate("일자")));// 리스트에 클래스단위로 넣는게 구조상 더 좋음 타입이
																					// 여러개가 들어갈수 있으므로
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		dbClose();
		return listDailyMoney;
	}

}
