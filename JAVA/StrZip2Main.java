
public class StrZip2Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StrZip2 sz = new StrZip2();
		String str = "aaabbcccddaaffessk";
		String result = sz.getZip(str);
		System.out.println(result);
		
		// 압축된 문자열 풀기

		String zipString = "a1b2c3a2c4e1";
		String result2 = sz.getRelease(zipString);
		System.out.println(result2);
		

	}

}
