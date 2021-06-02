
public class StrZip2 {

	void StrZip2() {
	}

	public static String getZip(String str) {
		String zipStr = "";
		int cnt = 1;
		for (int i = 0; i < str.length(); i++) {

			for (int k = i + 1; k < str.length(); k++) {
				char ichar = str.charAt(i);
				char kchar = str.charAt(k);
				if (ichar == kchar) {
					cnt++;
				} else {
					zipStr += ichar;
					zipStr += cnt;
					i = k;
					cnt = 1;
				}
				if (k == str.length() - 1) {
					zipStr += kchar;
					zipStr += cnt;
				}

			}

		}

		return zipStr;
	}

	public static String getRelease(String zipString) {
		String release = "";
		String num = "";
		for (int i = 0; i < zipString.length(); i++) {
			char a = zipString.charAt(i);
			if (Character.isDigit(a) == false) {// 문자일때
				release += a;
			} else {// 숫자일때
				if (i == zipString.length() - 1) {
					num += a;
					int number = Integer.parseInt(num);
					if (number == 1) {
						num = "";
					}
					for (int k = 1; k < number; k++) {
						var j = release.charAt(release.length() - 1);
						release += j;
						num = "";

					}
					break;
				}
				if (Character.isDigit(zipString.charAt(i + 1)) == true) {
					num += a;
				} else {
					num += a;
					int number = Integer.parseInt(num);
					if (number == 1) {
						num = "";
					}
					for (int k = 1; k < number; k++) {
						var j = release.charAt(release.length() - 1);
						release += j;
						num = "";
					}

				}

			}
		}

		return release;

	}

}
