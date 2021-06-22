package model;

import java.security.Principal;
import java.security.acl.Group;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;

public class GroupcodeDAOImpl extends DAOBase implements GroupcodeDAO {


	@Override
	public List<GroupcodeVO> list() {
		Connection conn = getConnection();
		PreparedStatement stmt = null;
		ResultSet rs = null;
		List<GroupcodeVO> list = new ArrayList<>();
		// 2.연결커넥션을 가지고 쿼리보내서 작업하고
		try {
			stmt = conn.prepareStatement("select * from groupcode");
			rs = stmt.executeQuery();
			while (rs.next()) {
				GroupcodeVO gvo = new GroupcodeVO();
				gvo.setGcode(rs.getString(1));
				gvo.setGname(rs.getString(2));
				list.add(gvo);
			}
			return list;
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			// 3.db끊기
			closeDBResources(rs, stmt, conn);
		}
		return null;
		
	}

}
