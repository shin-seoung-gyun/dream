package model;

import javax.servlet.http.HttpServletRequest;

public class Sum {
	
	public static int result(HttpServletRequest request) {
		int sum = 0;
		int num1 = Integer.parseInt(request.getParameter("num1"));
		int num2 = Integer.parseInt(request.getParameter("num2"));
		for(int i = num1; i<=num2; i++) {
			sum+=i;
		}
		return sum;
	}
}
