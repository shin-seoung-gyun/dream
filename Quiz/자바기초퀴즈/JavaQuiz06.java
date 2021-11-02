package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz06 {

	public static void main(String[] args) {
		
//		[문제6] 다음을 입력받아 계산하시오
//        (삼각형넓이 = (밑변 * 높이)/2)  
//--입력--
//**** 삼각형의 넓이 구하기  ****
//밑변 :  10  
//높이 :   3
//--출력--
//넓이 :   XX.XX  <--- 소수 2자리까지출력하시오
		Scanner sc = new Scanner(System.in);
		System.out.println("**** 삼각형의 넓이 구하기 ****");
		System.out.print("밑변 : ");
		int bottom = sc.nextInt();
		System.out.print("높이 : ");
		int height = sc.nextInt();
		double triangle = (double)bottom*height/2;
		System.out.printf("넓이 : %.2f",triangle);
		
		
		
		
		
	}

}
