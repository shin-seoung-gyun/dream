package test;

import java.sql.Connection;

import model.DAOBase;

public class DAOBaseTest {

	public static void main(String[] args) {
		DAOBase daoBase = new DAOBase();
		Connection conn=daoBase.getConnection();
		daoBase.closeDBResources(null, null, conn);
		
		
		
	}

}
