package model;

import java.util.List;

public interface ProductDAO {
	//삽입쿼리
	public int create(ProductVO vo);
	//항목조회
	public ProductVO readOne(ProductVO vo);
	//우선생산조회 (제품이름, 생산 수량)
	List<FirstMakeVO> readFirstMakeList();
	//이익제품조회 (제품이름, 이익금액)
	List<ProfitRankVo> readProfitRankList();
	//그룹별 재고수량 조회(그룹코드, 재고수량)
	List<GroupJnumVO> readGroupJnumList();
	//항목수정
	public int update(ProductVO vo);
	//항목삭제
	public int delete(ProductVO vo);
	
	
}
