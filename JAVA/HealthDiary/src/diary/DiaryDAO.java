package diary;

import java.util.List;

public interface DiaryDAO {

	List<DiaryListVO> searchDate(DiaryListVO vo);//날자만 입력받아 검색하는 매서드
	
	DiaryListVO searchDateTime(DiaryListVO vo); //날짜,시간을 입력받아 검색하는 매서드
	
	void update(DiaryListVO vo);//검색한 후 수정한 내용을 db로 보내는 매서드
	
	void delete(DiaryListVO vo);//검색한 후 삭제하는  매서드
	
	void insert(DiaryListVO vo);//삽입
	
}



