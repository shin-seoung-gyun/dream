
public class ScreenOut {
	static void menu() {
		System.out.println("-----------------------------------");
		System.out.println("\t용돈 기입장\n");
		System.out.println("\t1.지출 입력");
		System.out.println("\t2.수입 입력");
		System.out.println("\t3.잔액 확인");
		System.out.println("\t4.전체 조회");
		System.out.println("\t5.마지막입력 취소");
		System.out.println("\t6.지출액 1~3위 조회");
		System.out.println("\t7.기간별 수입합계 지출합계 조회");
		System.out.println("\t8.기간별 수입평균 지출평균 조회");
		System.out.println("\t9.일별 수입,지출 조회");
		System.out.println("\t0.종료\n");
		System.out.println("\t 메뉴번호를 입력하세요.");
		System.out.println("-----------------------------------");
		System.out.print("입력 > ");

	}
	static void startDay() {
		System.out.println("\t시작일을 입력하세요.\n\tex) 2000-01-23.");
		System.out.print("입력 > ");
	}
	static void endDay() {
		System.out.println("\t종료일을 입력하세요.\n\tex) 2000-01-23.");
		System.out.print("입력 > ");
	}

	static void outItem() {
		System.out.println("\t지출한 내역을 입력하세요.\n\tex) 과자, 병원진료 등.");
		System.out.print("입력 > ");
	}

	static void inItem() {
		System.out.println("\t수입 내역을 입력하세요.\n\tex) 월급, 용돈 등.");
		System.out.print("입력 > ");
	}

	static void outMoney() {
		System.out.println("\t지출한 금액을 입력하세요.\n\tex) 1000, 30000 등.");
		System.out.print("입력 > ");
	}

	static void inMoney() {
		System.out.println("\t수입 금액을 입력하세요.\n\tex) 1000, 30000 등.");
		System.out.print("입력 > ");
	}

	static void checkMent(String item, String money, String inOut) {
		System.out.println("\t" + item + "이(가)" + money + "원 만큼 " + inOut + "이 맞습니까?");
		System.out.println("\t1)예\t2)아니오");
		System.out.print("입력 > ");
	}
	static void checkDayMent(String item, String money, String inOut) {
		System.out.println("\t" + item + "일 부터" + money + "일 까지 " + inOut + "이 맞습니까?");
		System.out.println("\t1)예\t2)아니오");
		System.out.print("입력 > ");
	}

	static void yesMent() {
		System.out.println("\t확인 되었습니다.");
	}

	static void noMent() {
		System.out.println("\t취소 되었습니다.");
	}

}
