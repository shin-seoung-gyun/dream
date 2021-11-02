package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz07 {

	public static void main(String[] args) {
//		[문제7] 키보드로 수를 입력받아 두수중 큰수를 출력하시오
//        (단, 비교연산은 삼항연산자를 이용하시오)
//Input a : 5
//Input b : 13
//큰수 : 13
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
		
		
		System.out.println("큰수 : "+large);
		
		
		
	}

}
