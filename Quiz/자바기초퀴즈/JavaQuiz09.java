package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz09 {

	public static void main(String[] args) {

//[����9] �Էµ� ���ڰ� �빮���̸� �ҹ��ڷ� ����ϰ�
//        �ҹ����̸� �빮�ڷ� ��ȯ�Ͽ� ����Ͻÿ�
//        �׿��� �����̸� "�Էµ���Ÿ����"��� ǥ���Ͻÿ�
//        (if-else�� �̿�)   
//Input Character: A
//result : a
//Input Character: a
//result : A
//Input Character: *
//�Էµ����� ����
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
			System.out.println("�Էµ����� ����");
		}
		
		
		
		
		
		
		
		
		
	}

}
