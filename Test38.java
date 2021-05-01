

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
			result = "저체중";
		}else if(91<=fat&&110>=fat) {
			result = "정상(표준체중)";
		}else if(111<=fat&&120>=fat) {
			result = "과체중";
		}else if(121<=fat&&130>=fat) {
			result = "경도비만";
		}else if(131<=fat&&150>=fat) {
			result = "중도비만";
		}else {
			result = "고도비만";
		}
	}
	
	public void output2() {
		output();
		System.out.printf("\n당신은 비만도 %.2f이고, %s입니다.",fat,result);
	}
	
	
	public static void main(String[] args) {
		
		Test38 t = new Test38();
		t.input();
		t.claculate();
		t.output2();
		
		
		
		
		
		
		
		
		
		
		
		
		
	}
}
