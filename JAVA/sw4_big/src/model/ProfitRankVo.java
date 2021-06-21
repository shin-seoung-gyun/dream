package model;

public class ProfitRankVo {
	private String pname;
	private String profit;
	@Override
	public String toString() {
		return "ProfitRankVo [pname=" + pname + ", profit=" + profit + "]";
	}
	public String getPname() {
		return pname;
	}
	public void setPname(String pname) {
		this.pname = pname;
	}
	public String getProfit() {
		return profit;
	}
	public void setProfit(String profit) {
		this.profit = profit;
	}
}
