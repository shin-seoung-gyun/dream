package memo;

import java.util.ArrayList;

public class Sv {
	//1.�޸� �� ��
	int insert(DtoMemo dto) {
		Dao dao = new Dao();
		return dao.insert(dto);
	}
	//2. ���
	ArrayList<DtoMemo> list(int page){
		Dao dao = new Dao();
		return dao.list(page);
	}
	//3. �� ����
	int count() {
		Dao dao = new Dao();
		return dao.count();
	}
	//4. ���� ���� ���� �� ����� �۰���
	DtoBest best() {
		Dao dao = new Dao();
		return dao.best();
	}
	
}
