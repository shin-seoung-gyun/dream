
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		DBAccess da = new DBAccess();// 클래스 임포트
		SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
		Date date = new Date();
		while (true) {

			ScreenOut.menu();
			switch (in.nextLine()) {
			case "1":// 지출
			{
				ScreenOut.outItem();
				String item = in.nextLine();
				ScreenOut.outMoney();
				String money = in.nextLine();
				ScreenOut.checkMent(item, money, "지출");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					String strDate = format.format(date).toString();
					da.insertRow(item, "-" + money,strDate);// INSERT DATA 함수 필요 지출탭이라 -추가
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;
			}
			case "2":// 수입
			{
				ScreenOut.inItem();
				String item = in.nextLine();
				ScreenOut.inMoney();
				String money = in.nextLine();
				ScreenOut.checkMent(item, money, "수입");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					String strDate = format.format(date).toString();
					da.insertRow(item, money,strDate);// INSERT DATA 함수 필요//abs?
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;

			}
			case "3":// 잔액
			{
				int sumMoney = da.getMoneyBalance();// 잔액 결과값 가져오는 함수 필요
				System.out.println("\t현재남은 금액은 " + sumMoney + "원 입니다.");
				System.out.println("Enter");
				in.nextLine();
				break;
			}

			case "4":// 전체조회
			{
				System.out.println("\t전체 목록을 조회합니다.");
				System.out.println("Enter");
				in.nextLine();
				System.out.println("\t지출(수입)내역\t금액\t\t날짜.");
				System.out.println("\t************************************");
				var listItem = da.selectAllItem();// 전체 조회 값 가져오는 함수 필요
				for (var item : listItem) {// for문 활용 내용 표시
					System.out.print("\t" + item.item);
					if (item.item.length() < 7) {
						System.out.print("\t");
					}

					System.out.print("\t" + item.money);
					if (item.money.length() < 10) {
						System.out.print("\t");
					}

					SimpleDateFormat format1 = new SimpleDateFormat("yyyy-MM-dd");
					System.out.print("\t" + format1.format(item.date1) + "\n");// 수정중 데이트타입으로 형변환 필요

				}
				break;
			}

			case "5":// 마지막 입력 취소
			{
				System.out.println("\t마지막 입력을 취소합니다.");
				System.out.println("Enter");
				in.nextLine();
				da.lastOrderCancle();
				break;
			}
			case "6":// 지출액 1~3위 조회
			{
				System.out.println("\t지출액 1~3위를 조회합니다.");
				System.out.println("Enter");
				in.nextLine();

				System.out.println("\t지출내역\t\t금액.");
				System.out.println("\t************************************");

				var rankItem = da.outPocket();// 전체 조회 값 가져오는 함수 필요
				for (var item1 : rankItem) {// for문 활용 내용 표시
					System.out.print("\t" + item1.item);
					if (item1.item.length() < 7) {
						System.out.print("\t");
					}
					System.out.print("\t" + item1.money + "\n");

				}

			}
			case "7": {
				System.out.println("\t기간별 수입합계, 지출합계를 조회합니다.");
				ScreenOut.startDay();
				String start = in.nextLine();
				ScreenOut.endDay();
				String end = in.nextLine();
				System.out.println("Enter");
				in.nextLine();
				
				ScreenOut.checkDayMent(start, end, "기간");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					System.out.println("\t총수입내역\t\t총지출내역.");
					System.out.println("\t************************************");

					var listDaily = da.dailyInOut(start, end);
					for (var item2 : listDaily) {// for문 활용 내용 표시
						System.out.print("\t" + item2.item);//총수입
						if (item2.item.length() < 7) {
							System.out.print("\t");
						}
						System.out.print("\t\t" + item2.money + "\n");//총지출
					}
					
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;
			}
			
			case "8": {
				System.out.println("\t기간별 수입평균, 지출평균를 조회합니다.");
				ScreenOut.startDay();
				String start = in.nextLine();
				ScreenOut.endDay();
				String end = in.nextLine();
				System.out.println("Enter");
				in.nextLine();
				
				ScreenOut.checkDayMent(start, end, "기간");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					System.out.println("\t수입평균내역\t\t지출평균내역.");
					System.out.println("\t************************************");

					var listDailyAvg = da.dailyInOutAvg(start, end);
					for (var item2 : listDailyAvg) {// for문 활용 내용 표시
						System.out.print("\t" + item2.item);//총수입
						if (item2.item.length() < 7) {
							System.out.print("\t");
						}
						System.out.print("\t\t" + item2.money + "\n");//총지출
					}
					
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;
			}
			
			case "9": {
				System.out.println("\t일별 수입, 지출를 조회합니다.");
				ScreenOut.startDay();
				String start = in.nextLine();
				ScreenOut.endDay();
				String end = in.nextLine();
				System.out.println("Enter");
				in.nextLine();
				
				ScreenOut.checkDayMent(start, end, "기간");
				String check = in.nextLine();
				if (check.equals("1")) {
					ScreenOut.yesMent();
					System.out.println("\t수입,지출내역\t\t일자.");
					System.out.println("\t************************************");

					var dailyListMoney = da.dailyInOutMoney(start, end);
					for (var item2 : dailyListMoney) {// for문 활용 내용 표시
						System.out.print("\t" + item2.item);//수입 지출
						if (item2.item.length() < 10) {
							System.out.print("\t");
						}
						SimpleDateFormat format1 = new SimpleDateFormat("yyyy-MM-dd");
						System.out.print("\t\t" + format1.format(item2.date1) + "\n");//일자
					}
					
				} else {
					ScreenOut.noMent();
				}
				System.out.println("Enter");
				in.nextLine();
				break;
			}

			case "0":// 종료
			{
				System.out.println("종료되었습니다.");
				return;
			}
			default:
				System.out.println("잘못입력하셨습니다. 다시 입력하세요");
				break;

			}
		}
	}

}
