package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz09 {

	public static void main(String[] args) {

//[문제9] 입력된 문자가 대문자이면 소문자로 출력하고
//        소문자이명 대문자로 변환하여 출력하시오
//        그외의 문자이면 "입력데이타오류"라고 표시하시오
//        (if-else문 이용)   
//Input Character: A
//result : a
//Input Character: a
//result : A
//Input Character: *
//입력데이터 오류
		Scanner sc = new Scanner(System.in);
		System.out.print("Input Character : ");
		String ch = sc.next();
		if(Character.isAlphabetic(ch.charAt(0))==true) {
			if(Character.isUpperCase(ch.charAt(0))==true) {
				char result = Character.toLowerCase(ch.charAt(0));
				System.out.println("result : "+result);
			}else {
				char result = Character.toUpperCase(ch.charAt(0));
				System.out.println("result : "+result);
			}
			
		}else {
			System.out.println("입력데이터 오류");
		}
		
		
		
		
		
		
		
		
		
	}

}
