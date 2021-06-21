package model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class ProductDAOImpl extends DAOBase implements ProductDAO {

	@Override
	public int create(ProductVO vo) {
		// 1.db연결
		Connection conn = getConnection();
		PreparedStatement stmt = null;
		// 2.연결커넥션을 가지고 쿼리보내서 작업하고
		try {
			stmt = conn.prepareStatement(
					"INSERT INTO `product` (`code`, `pname`, `cost`, `pnum`, `jnum`, `sale`, `gcode`) VALUES (?,?, ?, ?, ?, ?, ?)");
			stmt.setString(1, vo.getCode());
			stmt.setString(2, vo.getPname());
			stmt.setInt(3, vo.getCost());
			stmt.setInt(4, vo.getPnum());
			stmt.setInt(5, vo.getJnum());
			stmt.setInt(6, vo.getSale());
			stmt.setString(7, vo.getGcode());
			return stmt.executeUpdate();// 리턴 안받아도 될때

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			// 3.db끊기
			closeDBResources(null, stmt, conn);
		}
		return 0;
	}

	@Override
	public ProductVO readOne(ProductVO vo) {
		// 1.db연결
		Connection conn = getConnection();
		PreparedStatement stmt = null;
		ResultSet rs = null;
		ProductVO vio = new ProductVO();
		// 2.연결커넥션을 가지고 쿼리보내서 작업하고
		try {
			stmt = conn.prepareStatement(
					"select * from product, groupcode where product.gcode=groupcode.gcode and code = ?");
			stmt.setString(1, vo.getCode());
			
			rs = stmt.executeQuery();
			rs.next();
			vio.setCode(rs.getString(1));
			vio.setPname(rs.getString(2));
			vio.setCost(rs.getInt(3));
			vio.setPnum(rs.getInt(4));
			vio.setJnum(rs.getInt(5));
			vio.setSale(rs.getInt(6));
			vio.setGcode(rs.getString(7));

			return vio;

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			// 3.db끊기
			closeDBResources(rs, stmt, conn);
		}

		return null;
	}

	@Override
	public List<FirstMakeVO> readFirstMakeList() {
		Connection conn = getConnection();
		PreparedStatement stmt = null;
		ResultSet rs = null;
		List<FirstMakeVO> list = new ArrayList<>();
		// 2.연결커넥션을 가지고 쿼리보내서 작업하고
		try {
			stmt = conn.prepareStatement("select pname, pnum-jnum as 생산수량  from product where jnum<(pnum*0.2)");
			rs = stmt.executeQuery();
			while (rs.next()) {
				FirstMakeVO fvo = new FirstMakeVO();
				fvo.setPname(rs.getString(1));
				fvo.setJnum(rs.getInt(2));
				list.add(fvo);
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

	@Override
	public List<ProfitRankVo> readProfitRankList() {//확인해야함
		Connection conn = getConnection();
		PreparedStatement stmt = null;
		ResultSet rs = null;
		List<ProfitRankVo> list = new ArrayList<>();
		// 2.연결커넥션을 가지고 쿼리보내서 작업하고
		try {
			stmt = conn.prepareStatement("select pname, jnum*(sale-cost) as 수익  from product order by 수익 desc");
			rs = stmt.executeQuery();
			while (rs.next()) {
				ProfitRankVo pf = new ProfitRankVo();
				pf.setPname(rs.getString(1));
				pf.setProfit(rs.getString(2));
				list.add(pf);
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

	@Override
	public List<GroupJnumVO> readGroupJnumList() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public int update(ProductVO vo) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int delete(ProductVO vo) {
		// TODO Auto-generated method stub
		return 0;
	}

}
