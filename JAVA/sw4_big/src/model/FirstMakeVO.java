package model;

public class FirstMakeVO {
	private String pname;
	private int jnum;
	public String getPname() {
		return pname;
	}
	public void setPname(String pname) {
		this.pname = pname;
	}
	public int getJnum() {
		return jnum;
	}
	public void setJnum(int jnum) {
		this.jnum = jnum;
	}
	@Override
	public String toString() {
		return "FirstMakeVO [pname=" + pname + ", jnum=" + jnum + "]";
	}
	
}
