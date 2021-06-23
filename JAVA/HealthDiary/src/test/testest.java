package test;


import java.util.List;

import diary.DiaryDAOImpl;
import diary.DiaryListVO;

public class testest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		DiaryDAOImpl dd = new DiaryDAOImpl();
		DiaryListVO vo = new DiaryListVO();
//		vo.setDate("2021-06-23 11:32:11");
		vo.setTitle("테스트3");
		vo.setContents("테스트테스트3");
//		ArrayList<DiaryListVO> ddlist = new ArrayList<DiaryListVO>();
//		List<DiaryListVO> ddlist = dd.searchDate(vo);
//		for(DiaryListVO temp : ddlist) {
//			System.out.println(temp.getTitle());
//			System.out.println(temp.getDate());
//		}
//		System.out.println(dd.searchDateTime(vo));
//		dd.update(vo);
//		dd.delete(vo);
		dd.insert(vo);
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	}
	
	
	

}
