package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz08 {

	public static void main(String[] args) {
		
//		[문제8] 값을 입력받아 0보다 작거나 100보다 크면 "입력오류!!"  출력
//        (if문과 ||연산자를 이용하시오)
//점수입력 : 120
//입력오류!!
//점수입력 : 55
//입력된값 : 55		
		
		Scanner sc = new Scanner(System.in);
		System.out.println("점수입력 : ");
		int a = sc.nextInt();
		if(a<0||a>100) {
			System.out.println("입력오류!!");
		}else {
			System.out.println("입력된값 : "+a);
		}
		
		
		
		
		
		
		
		
		
	}

}
