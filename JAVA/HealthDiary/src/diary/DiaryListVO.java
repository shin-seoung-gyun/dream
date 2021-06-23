package diary;

public class DiaryListVO {// 날자로 검색해서 나온 결과를 제목과 내용, 날자를 옮기는 데이터
	private String title;
	private String contents;
	private String date;
	public String getDate() {
		return date;
	}
	public void setDate(String date) {
		this.date = date;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getContents() {
		return contents;
	}
	public void setContents(String contents) {
		this.contents = contents;
	}
	@Override
	public String toString() {
		return "DiaryListVO [title=" + title + ", contents=" + contents + "]";
	}
	
	
}
