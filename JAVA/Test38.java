

public class Test38 extends Health{
	double s_weight = 0.0;
	double fat = 0.0;
	String result = null;
	
	
	public Test38() {
		super();
	}

	public Test38(char gender, double tall, double weight, double s_weight,
					double fat, String result) {
		
		super(gender, tall, weight);
		this.s_weight = s_weight;
		this.fat = fat;
		this.result = result;
	}
	
	@Override
	public void input() {
		// TODO Auto-generated method stub
		super.input();
	}
	
	public void claculate() {
		if (gender == 'M') {
			s_weight = (tall-100)*0.9;
			fat= weight/s_weight*100;
		} else if(gender == 'W') {
			s_weight = (tall-100)*0.85;
			fat= weight/s_weight*100;
		} 
		
		if(fat <=90) {
			result = "��ü��";
		}else if(91<=fat&&110>=fat) {
			result = "����(ǥ��ü��)";
		}else if(111<=fat&&120>=fat) {
			result = "��ü��";
		}else if(121<=fat&&130>=fat) {
			result = "�浵��";
		}else if(131<=fat&&150>=fat) {
			result = "�ߵ���";
		}else {
			result = "����";
		}
	}
	
	public void output2() {
		output();
		System.out.printf("\n����� �񸸵� %.2f�̰�, %s�Դϴ�.",fat,result);
	}
	
	
	public static void main(String[] args) {
		
		Test38 t = new Test38();
		t.input();
		t.claculate();
		t.output2();
		
		
		
		
		
		
		
		
		
		
		
		
		
	}
}
