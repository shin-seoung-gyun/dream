package memo;

import java.util.ArrayList;

public interface DaoInter {
	//1.�޸� �� ��
	int insert(DtoMemo dto);
	//2. ���
	ArrayList<DtoMemo> list(int page);
	//3. �� ����
	int count();
	//4. ���� ���� ���� �� ����� �۰���
	DtoBest best();
	//������ �ѹ�
	int lastnum();
	//�˻����
	ArrayList<DtoMemo> searchList(String search, int page);
	
}
