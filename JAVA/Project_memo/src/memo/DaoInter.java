package memo;

import java.util.ArrayList;

public interface DaoInter {
	//1.메모 삽 입
	int insert(DtoMemo dto);
	//2. 출력
	ArrayList<DtoMemo> list(int page);
	//3. 글 개수
	int count();
	//4. 가장 많은 글을 쓴 사람과 글개수
	DtoBest best();
	//마지막 넘버
	int lastnum();
	//검색기능
	ArrayList<DtoMemo> searchList(String search, int page);
	
}
