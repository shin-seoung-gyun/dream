package JavaQuiz;

public class JavaQuiz04 {

	public static void main(String[] args) {

//[����4] ���������� �����Ͽ� ����Ͻÿ�
//   ����1) data�� ��ȿ��, ���ߺ�, �븮, 1500000�� ����
//          �������� ����  name,department,position,sal�� �Ұ�
//   ����2)����� �Ʒ��� ���� �޼���(�Լ�)�� �̿��Ͻÿ�
//--���--
//�̸� : ��ȿ��     ---> println
//�μ� : ���ߺ�     ---> printf  
//���� : �븮       ---> print 1�����Ἥ ����,�޿����
//�޿� : 1500000��
		
		String name = "��ȿ��";
		String department = "���ߺ�";
		String position = "�븮";
		int sal = 1500000;
		System.out.println("�̸� = "+name);
		System.out.printf("�μ� = "+department+"\n");
		System.out.print("���� = "+position+"\n"+"�޿� = "+sal);
		
	}

}
