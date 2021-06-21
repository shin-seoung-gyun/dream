package model;

public class GroupJnumVO {

	private String gcode;
	private int jnum;
	@Override
	public String toString() {
		return "GroupJnumVo [gcode=" + gcode + ", jnum=" + jnum + "]";
	}
	public String getGcode() {
		return gcode;
	}
	public void setGcode(String gcode) {
		this.gcode = gcode;
	}
	public int getJnum() {
		return jnum;
	}
	public void setJnum(int jnum) {
		this.jnum = jnum;
	}
}
