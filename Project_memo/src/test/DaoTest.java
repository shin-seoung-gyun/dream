package test;

import java.util.ArrayList;

import memo.Dao;
import memo.DtoBest;
import memo.DtoMemo;

public class DaoTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Dao dao = new Dao();
		System.out.println("글갯수"+dao.count());
		DtoMemo dto = new DtoMemo();
		dto.setName("테스트");
		dto.setMemo("이것은 테스트 메모");
		dao.insert(dto);
		DtoBest best = dao.best();
		System.out.println(best);
		ArrayList<DtoMemo> list = dao.list(2);
		for(DtoMemo temp : list) {
			System.out.println(temp);
		}
		
	}

}
