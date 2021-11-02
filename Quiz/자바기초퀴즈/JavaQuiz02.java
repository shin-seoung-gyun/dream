package JavaQuiz;

public class JavaQuiz02 {

	public static void main(String[] args) {
		//[문제2]65430원을 만들기 위한 화폐의 갯수를 구하시오.
		//money = 65430원
		int money = 65430;
		int ten = money/10%10;
		System.out.println("십원 = "+ten);
		int hun = money/100%10;
		System.out.println("백원 = "+hun);
		int thousand = money/1000%10;
		System.out.println("천원 = "+thousand);
		int tenthousand = money/10000%10;
		System.out.println("만원 = "+tenthousand);
	}

}
