package memo;

import java.util.ArrayList;

public class Sv {
	//1.메모 삽 입
	int insert(DtoMemo dto) {
		Dao dao = new Dao();
		return dao.insert(dto);
	}
	//2. 출력
	ArrayList<DtoMemo> list(int page){
		Dao dao = new Dao();
		return dao.list(page);
	}
	//3. 글 개수
	int count() {
		Dao dao = new Dao();
		return dao.count();
	}
	//4. 가장 많은 글을 쓴 사람과 글개수
	DtoBest best() {
		Dao dao = new Dao();
		return dao.best();
	}
	int analysis() {
		Dao dao = new Dao();
		int result =  dao.lastnum();
		return result;
	}
	ArrayList<DtoMemo> searchList(String search,int page){
		Dao dao = new Dao();
		return dao.searchList(search, page);
	}
}
