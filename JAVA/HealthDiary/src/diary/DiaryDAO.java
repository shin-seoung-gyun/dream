package diary;

import java.util.List;

public interface DiaryDAO {

	List<DiaryListVO> searchDate(DiaryListVO vo);//���ڸ� �Է¹޾� �˻��ϴ� �ż���
	
	DiaryListVO searchDateTime(DiaryListVO vo); //��¥,�ð��� �Է¹޾� �˻��ϴ� �ż���
	
	void update(DiaryListVO vo);//�˻��� �� ������ ������ db�� ������ �ż���
	
	void delete(DiaryListVO vo);//�˻��� �� �����ϴ�  �ż���
	
	void insert(DiaryListVO vo);//����
	
}



