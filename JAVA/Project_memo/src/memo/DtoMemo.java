package memo;

import java.util.Date;

public class DtoMemo {
	private int no;
	private String name;
	private String memo;
	
	private String time;
	
	public int getNo() {
		return no;
	}
	public void setNo(int no) {
		this.no = no;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getMemo() {
		return memo;
	}
	public void setMemo(String memo) {
		this.memo = memo;
	}
	public String getTime() {
		return time;
	}
	public void setTime(String time) {
		this.time = time;
	}
	@Override//어노테이션이 이메서드가 오버라이드된 메서드임을 컴파일러에게 알려줌
	public String toString() {
		return "DtoMemo [no=" + no + ", name=" + name + ", memo=" + memo + ", time=" + time + "]";
	}

}
