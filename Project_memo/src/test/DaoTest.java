package test;

import java.util.ArrayList;

import memo.Dao;
import memo.DtoBest;
import memo.DtoMemo;

public class DaoTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Dao dao = new Dao();
		System.out.println("�۰���"+dao.count());
		DtoMemo dto = new DtoMemo();
		dto.setName("�׽�Ʈ");
		dto.setMemo("�̰��� �׽�Ʈ �޸�");
		dao.insert(dto);
		DtoBest best = dao.best();
		System.out.println(best);
		ArrayList<DtoMemo> list = dao.list(2);
		for(DtoMemo temp : list) {
			System.out.println(temp);
		}
		
	}

}
