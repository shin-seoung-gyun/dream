package test;

import java.util.List;

import model.FirstMakeVO;
import model.ProductDAOImpl;
import model.ProductVO;

public class ProductDAOimpltest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ProductVO vo = new ProductVO();
		
		vo.setCode("A03");
//		vo.setPnum(100);
//		vo.setCost(200);
//		vo.setGcode("A");
//		vo.setPname("난제품");
//		vo.setSale(300);
//		vo.setJnum(150);
//		
//		ProductDAOImpl pdao = new ProductDAOImpl();
//		System.out.println(pdao.create(vo));
//		
		ProductDAOImpl pdao = new ProductDAOImpl();
//		List<FirstMakeVO> list =pdao.readFirstMakeList();
//		
//		for(FirstMakeVO fvo:list) {
//			System.out.println(fvo.toString());
//			System.out.println(fvo.getPname());
//			System.out.println(fvo.getJnum());
//		}
		
		System.out.println(pdao.readOne(vo));
		
	}

}
