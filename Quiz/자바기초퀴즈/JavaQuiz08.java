package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz08 {

	public static void main(String[] args) {
		
//		[����8] ���� �Է¹޾� 0���� �۰ų� 100���� ũ�� "�Է¿���!!"  ���
//        (if���� ||�����ڸ� �̿��Ͻÿ�)
//�����Է� : 120
//�Է¿���!!
//�����Է� : 55
//�ԷµȰ� : 55		
		
		Scanner sc = new Scanner(System.in);
		System.out.println("�����Է� : ");
		int a = sc.nextInt();
		if(a<0||a>100) {
			System.out.println("�Է¿���!!");
		}else {
			System.out.println("�ԷµȰ� : "+a);
		}
		
		
		
		
		
		
		
		
		
	}

}
