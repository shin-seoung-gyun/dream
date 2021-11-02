package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz10 {

	public static void main(String[] args) {
//
//[문제10] 4개의 값을 콘솔에서 입력받아 처리하시오
//        조건) 성별 : M 이면 "남자", 나머지 "여자" 
//             (삼항연산자 이용)
//Input name: 장미란
//Input gender: F
//Input age:  25
//Input tall: 173.3 
//--결과--
//이름 : 장미란
//성별 : 여자 
//나이 : 25세
//신장 : 173.3cm  
		
		Scanner sc = new Scanner(System.in);
		System.out.print("Input name: ");
		String name = sc.next();
		System.out.print("Input gender: ");
		String gender = sc.next();
		System.out.print("Input age: ");
		int age = sc.nextInt();
		System.out.print("Input tall: ");
		double tall = sc.nextDouble();
		
		String gender2 = (gender.equals("M")?"남자":"여자");
		
		System.out.println("이름 : "+name);
		System.out.println("성별 : "+gender2);
		System.out.println("나이 : "+age+"세");
		System.out.printf("신장 : %.1f cm",tall);
		
		
	}

}
