import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		OutLine ot = new OutLine();
		Scanner in = new Scanner(System.in);
		DBAccess da = new DBAccess();
		RMForProject rm = new RMForProject();
		Date date = new Date();
		SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		
		while (true) {
			ot.menu();
			System.out.print("메뉴를 입력하세요.>");
			String userStr = in.nextLine();

			// 주소록보기
			if (userStr.equals("1")) {
				ot.menu2();
				System.out.print("메뉴를 입력하세요.>");
				String userStr2 = in.nextLine();

				if (userStr2.equals("1")) {
					System.out.println("\t전체 주소록을 불러옵니다.");
					da.allAddress();// 모든 주소록 불러오는 함수
				} else if (userStr2.equals("2")) {
					System.out.println("\t이름으로 검색을 시작합니다.");
					// 이름으로 검색하는 함수
					System.out.print("이름을 입력해 주세요.>");
					String name = in.nextLine();
					da.findNameAddress(name);
				} else if (userStr2.equals("3")) {
					System.out.println("\t소속으로 검색을 시작합니다.");
					// 소속으로 검색하는 함수
					System.out.print("소속을 입력해 주세요.>");
					String Affiliation = in.nextLine();
					da.findAffiliationAddress(Affiliation);
				} else {
					System.out.println("\t잘못입력하셨습니다. 처음으로 돌아갑니다.");
					continue;
				}

			} else if (userStr.equals("2")) {// 메일보내기
				ot.menu3();
				System.out.print("메뉴를 입력하세요.>");
				String userStr2 = in.nextLine();

				// 한명에게 메일 전송
				if (userStr2.equals("1")) {
					System.out.println("\t한명에게 메일을 보냅니다.");
					// 한명에게 메일 보낼 처리
					SMForProject sp = new SMForProject();
					System.out.print("받는 분의 메일 주소를 입력하세요.>");
					String reID = in.nextLine();
					// 해당 아이디가 주소록에 있으면 본문에 기본형식 출력
					System.out.print("제목>");
					String title = in.nextLine();
					System.out.print("본문>");
					String mainText = in.nextLine();
					// 아이디에 따라서 정보를 찾는 함수 필요.
					boolean sameAddress = da.isTure(reID);
					if (sameAddress == false) {
						sp.sendMail1(reID, title, mainText);
					} else {
						sp.sendMail1(reID, title, da.baseText(mainText, reID));
					}
					da.sendMail(reID, title, mainText, format.format(date));
					
					// 여러명에게 메일보낼 처리
				} else if (userStr2.equals("2")) {
					System.out.println("\t여러사람에게 메일을 보냅니다.");
					ot.menu4();
					System.out.print("메뉴를 입력하세요.>");
					String userStr3 = in.nextLine();

					if (userStr3.equals("1")) {// 주소록 전체 보내기
						System.out.println("전체 메일 발송합니다.");
						
						SMForProject sp = new SMForProject();
						System.out.print("제목>");
						String title = in.nextLine();
						System.out.print("본문>");
						String mainText = in.nextLine();
						// 전체 주소록의 email을 List로 불러오는 함수
						List<String> toList = da.allAddAry();
						// 위의 함수에서 받아온 메일 주소로 뿌리는 함수
						sp.sendAllMail(toList, title, mainText);
						for(int i = 0; i <toList.size();i++) {
							da.sendMail(toList.get(i), title, mainText, format.format(date));
						}

					} else if (userStr3.equals("2")) {// 소속 전체보내기
						System.out.println("소속 그룹발송합니다.");
						
						System.out.print("받으시는 분의 소속을 입력하세요.>");
						String reAffiliation = in.nextLine();
						SMForProject sp = new SMForProject();
						System.out.print("제목>");
						String title = in.nextLine();
						System.out.print("본문>");
						String mainText = in.nextLine();
						List<String> emailList = da.findAffAdd(reAffiliation);//소속으로 이메일리스트를 받아오는 함수
						for (int i = 0; i < emailList.size(); i++) {
							sp.sendMail1(emailList.get(i), title, da.baseText(mainText, emailList.get(i)));
							da.sendMail(emailList.get(i), title, mainText, format.format(date));
						}

					} else if (userStr3.equals("3")) {// 소속 및 부서 입력후 모두 보내기
						System.out.println("소속및 부서 그룹발송합니다.");
						System.out.print("받으시는 분의 소속을 입력하세요.>");
						String reAffiliation = in.nextLine();
						System.out.print("받으시는 분의 부서를 입력하세요.>");
						String divisions = in.nextLine();
						SMForProject sp = new SMForProject();
						System.out.print("제목>");
						String title = in.nextLine();
						System.out.print("본문>");
						String mainText = in.nextLine();
						List<String> emailList = da.findAffDivAdd(reAffiliation, divisions);//소속및 부서로 이메일리스트를 받아오는 함수
						for (int i = 0; i < emailList.size(); i++) {
							sp.sendMail1(emailList.get(i), title, da.baseText(mainText, emailList.get(i)));
							da.sendMail(emailList.get(i), title, mainText, format.format(date));
						}
					} else {
						System.out.println("\t잘못입력하셨습니다. 처음으로 돌아갑니다.");
						continue;
					}

				} else {
					System.out.println("\t잘못입력하셨습니다. 처음으로 돌아갑니다.");
					continue;
				}
			//받은 메일 확인하기
			} else if (userStr.equals("3")) {
				ot.menu5();
				System.out.print("메뉴를 입력하세요.>");
				String userStr2 = in.nextLine();
				if (userStr2.equals("1")){//전체 메일 확인
					System.out.println("전체 메일 상위 10개를 출력합니다");
					try {
						rm.reciveAllMail();
					} catch (Exception e) {
						// TODO: handle exception
						e.printStackTrace();
					}
				} else if (userStr2.equals("2")) {//읽지 않은 메일 확인
					System.out.println("읽지않은 받은 메일 상위 10개를 출력합니다");
					try {
						rm.reciveMail();
					} catch (Exception e) {
						// TODO: handle exception
						e.printStackTrace();
					}
				}
			//보낸 메일 확인하기	
			} else if (userStr.equals("4")) {	
				System.out.println("보낸 메일을 출력합니다.");
				da.findSendMail();
				
			} else if (userStr.equals("5")) {	//주소록 추가
				System.out.println("주소록을 추가합니다.");
				System.out.print("이름을 입력하세요>");
				String name = in.nextLine();
				System.out.print("소속을 입력하세요>");
				String affiliation = in.nextLine();
				System.out.print("부서를 입력하세요>");
				String divisions = in.nextLine();
				System.out.print("직급을 입력하세요>");
				String position = in.nextLine();
				System.out.print("연락처를 입력하세요>");
				String phone = in.nextLine();
				System.out.print("이메일주소를 입력하세요>");
				String eMail = in.nextLine();
				da.insertAB(name, divisions, position, phone, eMail, affiliation);
				
			} else if (userStr.equals("6")) {	// 주소록 수정 (no와 수정할 칼럼명 하나를 입력받고 수정할 내용 입력받은 후 수정)	
				System.out.println("주소록을 수정합니다.");
				System.out.println("주소록의 번호를 입력하세요>");
				int no = in.nextInt();
				in.nextLine();
				System.out.println("수정할 칼럼을 입력하세요. ex)이름,소속,직급,부서,연락처,이메일주소>");
				String column = in.nextLine();
				System.out.println("수정할 내용을 입력하세요>");
				String text = in.nextLine();
				da.setColumn(no, column, text);
				
			} else if (userStr.equals("7")) {	// 주소록 삭제 (no 입력받고 해당 no 행 삭제)	
				System.out.println("주소록을 삭제합니다.");
				System.out.println("주소록의 번호를 입력하세요>");
				int no = in.nextInt();
				in.nextLine();
				da.deleteDate(no);
				
			} else if (userStr.equals("0")) {//종료
				System.out.println("\t프로그램을 종료합니다.");
				break;
			}

		}

	}

}
