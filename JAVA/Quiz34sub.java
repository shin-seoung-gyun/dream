
public class Quiz34sub extends Quiz34 {
	
	String department;
	
	public Quiz34sub(String name, int salary, String department) {
		super(name, salary);
		// TODO Auto-generated constructor stub
		this.department=department;
	}

	public void getInfomation2() {
		System.out.printf("�μ� : %s",department);
	}
	
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	
		Quiz34sub  ob = new Quiz34sub("��ö����",85000000,"ö���");
		ob.getInfomation1();
		ob.getInfomation2();
		
		
		
	}

	

}
