package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz07 {

	public static void main(String[] args) {
//		[����7] Ű����� ���� �Է¹޾� �μ��� ū���� ����Ͻÿ�
//        (��, �񱳿����� ���׿����ڸ� �̿��Ͻÿ�)
//Input a : 5
//Input b : 13
//ū�� : 13
		Scanner sc = new Scanner(System.in);
		System.out.print("Input a : ");
		int a = sc.nextInt();
		System.out.print("Input b : ");
		int b = sc.nextInt();
		
		int large;
		if(a>b) {
			large = a;
		} else if (a<b) {
			large = b;
		} else {
			large = a;
		}
		
		
		System.out.println("ū�� : "+large);
		
		
		
	}

}
