package JavaQuiz;

import java.util.Scanner;

public class javaQuiz05 {

	public static void main(String[] args) {
//		[문제5] 다음을 입력받아 계산하시오
//		--입력--
//		Input name : 민들래
//		kor : 90 
//		eng : 70 
//		mat : 75
//		--출력--
//		이름 : 민들래
//		합계점수 : 235점
//		평균점수 :  78.3   <-- 소수 1자리까지출력하시오
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
		System.out.print("이름 = "+name);
		System.out.print("\n합계점수 = "+total);
		System.out.printf("\n평균점수 = %.1f",avg);
		
		
	}

}
