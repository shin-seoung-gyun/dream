package model;

public class GroupcodeVO {
	private String gcode;
	private String gname;
	@Override
	public String toString() {
		return "Groupcode [gcode=" + gcode + ", gname=" + gname + "]";
	}
	public String getGcode() {
		return gcode;
	}
	public void setGcode(String gcode) {
		this.gcode = gcode;
	}
	public String getGname() {
		return gname;
	}
	public void setGname(String gname) {
		this.gname = gname;
	}
}
