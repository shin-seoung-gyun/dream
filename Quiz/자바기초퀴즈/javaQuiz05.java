package JavaQuiz;

import java.util.Scanner;

public class javaQuiz05 {

	public static void main(String[] args) {
//		[����5] ������ �Է¹޾� ����Ͻÿ�
//		--�Է�--
//		Input name : �ε鷡
//		kor : 90 
//		eng : 70 
//		mat : 75
//		--���--
//		�̸� : �ε鷡
//		�հ����� : 235��
//		������� :  78.3   <-- �Ҽ� 1�ڸ���������Ͻÿ�
		Scanner sc = new Scanner(System.in);
		
		String name ="";
		int kor,eng,mat;
		System.out.print("Input name = ");
		name = sc.next();
		System.out.print("kor = ");
		kor = sc.nextInt();
		System.out.print("eng = ");
		eng = sc.nextInt();
		System.out.print("mat = ");
		mat = sc.nextInt();
		
		int total = kor+eng+mat;
		double avg = (double)total/3;
		System.out.print("�̸� = "+name);
		System.out.print("\n�հ����� = "+total);
		System.out.printf("\n������� = %.1f",avg);
		
		
	}

}
