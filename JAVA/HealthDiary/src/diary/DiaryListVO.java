package diary;

public class DiaryListVO {// ���ڷ� �˻��ؼ� ���� ����� ����� ����, ���ڸ� �ű�� ������
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
