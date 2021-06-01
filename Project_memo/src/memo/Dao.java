package memo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

public class Dao implements DaoInter {

	@Override
	public int insert(DtoMemo dto) {
		Connection conn=JdbcUtil.getConn();
		PreparedStatement pstmt=null;
		int count =-1;
		try {
			
			pstmt=conn.prepareStatement("INSERT INTO memo_table (name, memo) VALUES (?, ?)");
			pstmt.setString(1, dto.getName());
			pstmt.setString(2, dto.getMemo());
			
			count= pstmt.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {//무조건 실행됨.
			JdbcUtil.close(pstmt);
			JdbcUtil.close(conn);
		}
		return count;
	}

	@Override
	public ArrayList<DtoMemo> list(int page) {
		ArrayList<DtoMemo> list=new ArrayList<DtoMemo>();
		Connection conn = JdbcUtil.getConn();
		PreparedStatement pstmt = null;
		ResultSet result =null;
		try {
			pstmt = conn.prepareStatement("select * from memo_table order by no desc limit ?,10");
			pstmt.setInt(1, (page-1)*10);
			result = pstmt.executeQuery();
			while(result.next()) {
				DtoMemo dtoMemo = new DtoMemo();//와일문 밖에 만들면 마지막 데이터만 남아서 마지막 데이터만 반복됨.
				dtoMemo.setNo(result.getInt(1));
				dtoMemo.setName(result.getString(2));
				dtoMemo.setMemo(result.getString(3));
				dtoMemo.setTime(result.getString(4));
				list.add(dtoMemo);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			JdbcUtil.close(result);
			JdbcUtil.close(pstmt);
			JdbcUtil.close(conn);
		}
		
		return list;
		

	}

	@Override
	public int count() {
		Connection conn = JdbcUtil.getConn();
		int count=-1;
		PreparedStatement pstmt = null;
		ResultSet result =null;
		try {
			pstmt = conn.prepareStatement("select count(no) from memo_table");
			result = pstmt.executeQuery();
			result.next();
			count=result.getInt(1);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally {
			JdbcUtil.close(result);
			JdbcUtil.close(pstmt);
			JdbcUtil.close(conn);
		}
		
		return count;
	}

	@Override
	public DtoBest best() {
		Connection conn = JdbcUtil.getConn();
		DtoBest dtobest = null;
		PreparedStatement pstmt = null;
		ResultSet result =null;
		try {
			pstmt = conn.prepareStatement("select name, count(no) from memo_table GROUP BY name order by count(no) desc limit 0,1");
			result = pstmt.executeQuery();//결과를 가져와서 
			result.next();//첫번째 행을 가리키고
			dtobest = new DtoBest();//객체를 만들어서
			dtobest.setName(result.getString("name"));//값 넣는다.
			dtobest.setCount(result.getInt("count(no)"));//값 넣는다.
		} catch (SQLException e) {
		
			e.printStackTrace();
		}finally {
			JdbcUtil.close(result);
			JdbcUtil.close(pstmt);
			JdbcUtil.close(conn);
		}
		return dtobest;
	}

}
