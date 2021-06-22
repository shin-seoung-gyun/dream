package test;

import java.util.List;

import model.FirstMakeVO;
import model.GroupJnumVO;
import model.ProductDAOImpl;
import model.ProductVO;
import model.ProfitRankVo;

public class ProductDAOimpltest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ProductVO vo = new ProductVO();
		
		vo.setCode("A01");
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
//		List<ProfitRankVo> list = pdao.readProfitRankList();
//		for(ProfitRankVo pfr:list) {
//			System.out.println(pfr.getPname());
//			System.out.println(pfr.getProfit());
//		}
		
//		List<GroupJnumVO> list = pdao.readGroupJnumList();
//		for(GroupJnumVO gvo:list) {
//			System.out.println(gvo.getGcode());
//			System.out.println(gvo.getJnum());
//		}
		
		System.out.println(pdao.delete(vo));
		
//		System.out.println();
		
	}

}
