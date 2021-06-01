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
		} finally {//������ �����.
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
				DtoMemo dtoMemo = new DtoMemo();//���Ϲ� �ۿ� ����� ������ �����͸� ���Ƽ� ������ �����͸� �ݺ���.
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
			result = pstmt.executeQuery();//����� �����ͼ� 
			result.next();//ù��° ���� ����Ű��
			dtobest = new DtoBest();//��ü�� ����
			dtobest.setName(result.getString("name"));//�� �ִ´�.
			dtobest.setCount(result.getInt("count(no)"));//�� �ִ´�.
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
