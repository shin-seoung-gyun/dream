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
	@Override//������̼��� �̸޼��尡 �������̵�� �޼������� �����Ϸ����� �˷���
	public String toString() {
		return "DtoMemo [no=" + no + ", name=" + name + ", memo=" + memo + ", time=" + time + "]";
	}

}
