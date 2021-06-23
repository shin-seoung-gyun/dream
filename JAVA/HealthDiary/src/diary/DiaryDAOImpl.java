package diary;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class DiaryDAOImpl extends DAOBase implements DiaryDAO {

	@Override
	public List<DiaryListVO> searchDate(DiaryListVO vo) {// 날짜로 일기 리스트 받기
		Connection conn = getConnection();// db연결
		PreparedStatement stmt = null; // 쿼리 보내는 객체
		ResultSet rs = null;// 결과값 받는 객체
		List<DiaryListVO> volist = new ArrayList<DiaryListVO>();// 받아온 데이터를 담을 객체
		try {
			stmt = conn.prepareStatement("select * from diary where indate like ? '%'");
			stmt.setString(1, vo.getDate());
			System.out.println(vo.getDate());
			rs = stmt.executeQuery();
			while (rs.next()) {
				DiaryListVO dvo = new DiaryListVO();
				dvo.setTitle(rs.getString("title"));
				dvo.setDate(rs.getString("indate"));
				volist.add(dvo);
			}

			return volist;
		} catch (Exception e) {

		} finally {
			closeDBResources(rs, stmt, conn);
		}
		return null;
	}

	@Override
	public DiaryListVO searchDateTime(DiaryListVO vo) {// 날자 시간으로 일기 내용까지 받기
		Connection conn = getConnection();// db연결
		PreparedStatement stmt = null; // 쿼리 보내는 객체
		ResultSet rs = null;// 결과값 받는 객체
		DiaryListVO dvo = new DiaryListVO();
		try {
			stmt = conn.prepareStatement("select * from diary where indate = ?");
			stmt.setString(1, vo.getDate());
			rs = stmt.executeQuery();
			rs.next();
			dvo.setTitle(rs.getString("title"));
			dvo.setContents(rs.getString("contents"));
			dvo.setDate(rs.getString("indate"));

			return dvo;
		} catch (Exception e) {

		} finally {
			closeDBResources(rs, stmt, conn);
		}
		return null;
	}

	@Override
	public void update(DiaryListVO vo) {// 수정하는 매서드
		Connection conn = getConnection();// db연결
		PreparedStatement stmt = null; // 쿼리 보내는 객체

		try {
			stmt = conn.prepareStatement("UPDATE DIARY SET TITLE = ?, CONTENTS = ?,indate= ? WHERE indate=?");
			stmt.setString(4, vo.getDate());
			stmt.setString(3, vo.getDate());
			stmt.setString(1, vo.getTitle());
			stmt.setString(2, vo.getContents());
			stmt.executeUpdate();

		} catch (Exception e) {

		} finally {
			closeDBResources(null, stmt, conn);
		}

	}

	@Override
	public void delete(DiaryListVO vo) {// 삭제하는 매서드
		Connection conn = getConnection();// db연결
		PreparedStatement stmt = null; // 쿼리 보내는 객체

		try {
			stmt = conn.prepareStatement("delete from diary where indate=?");
			stmt.setString(1, vo.getDate());

			stmt.executeUpdate();

		} catch (Exception e) {

		} finally {
			closeDBResources(null, stmt, conn);
		}
	}

	@Override
	public void insert(DiaryListVO vo) {//일기 새로 등록하는 매서드
		// TODO Auto-generated method stub

		Connection conn = getConnection();// db연결
		PreparedStatement stmt = null; // 쿼리 보내는 객체

		try {
			stmt = conn.prepareStatement("INSERT INTO diary (`TITLE`,`CONTENTS`) VALUES (?,?)");
			stmt.setString(1, vo.getTitle());
			stmt.setString(2, vo.getContents());
			stmt.executeUpdate();

		} catch (Exception e) {

		} finally {
			closeDBResources(null, stmt, conn);
		}
		
	}

}
