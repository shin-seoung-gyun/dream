package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz06 {

	public static void main(String[] args) {
		
//		[����6] ������ �Է¹޾� ����Ͻÿ�
//        (�ﰢ������ = (�غ� * ����)/2)  
//--�Է�--
//**** �ﰢ���� ���� ���ϱ�  ****
//�غ� :  10  
//���� :   3
//--���--
//���� :   XX.XX  <--- �Ҽ� 2�ڸ���������Ͻÿ�
		Scanner sc = new Scanner(System.in);
		System.out.println("**** �ﰢ���� ���� ���ϱ� ****");
		System.out.print("�غ� : ");
		int bottom = sc.nextInt();
		System.out.print("���� : ");
		int height = sc.nextInt();
		double triangle = (double)bottom*height/2;
		System.out.printf("���� : %.2f",triangle);
		
		
		
		
		
	}

}
