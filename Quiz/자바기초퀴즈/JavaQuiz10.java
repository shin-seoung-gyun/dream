package JavaQuiz;

import java.util.Scanner;

public class JavaQuiz10 {

	public static void main(String[] args) {
//
//[����10] 4���� ���� �ֿܼ��� �Է¹޾� ó���Ͻÿ�
//        ����) ���� : M �̸� "����", ������ "����" 
//             (���׿����� �̿�)
//Input name: ��̶�
//Input gender: F
//Input age:  25
//Input tall: 173.3 
//--���--
//�̸� : ��̶�
//���� : ���� 
//���� : 25��
//���� : 173.3cm  
		
		Scanner sc = new Scanner(System.in);
		System.out.print("Input name: ");
		String name = sc.next();
		System.out.print("Input gender: ");
		String gender = sc.next();
		System.out.print("Input age: ");
		int age = sc.nextInt();
		System.out.print("Input tall: ");
		double tall = sc.nextDouble();
		
		String gender2 = (gender.equals("M")?"����":"����");
		
		System.out.println("�̸� : "+name);
		System.out.println("���� : "+gender2);
		System.out.println("���� : "+age+"��");
		System.out.printf("���� : %.1f cm",tall);
		
		
	}

}
