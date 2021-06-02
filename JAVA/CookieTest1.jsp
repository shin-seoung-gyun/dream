<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
쿠키를 테스트 합니다.
1.쿠키를 생성
<%
	Cookie cookie = new Cookie("name","honggildong");//쿠키의 이름과 값을 지정할수있다.
	cookie.setMaxAge(600);//초를 입력하여 만료기간을 설정할수 있음.
	response.addCookie(cookie);//서버에서 쿠키를 만들어 클라이언트로 보냄.
%>
<a href = "CookieTest2.jsp">쿠키값 불러오기</a>
</body>
</html>