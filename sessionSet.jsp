<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%
	session.setAttribute("name", "honggildong");
	session.setAttribute("pw", "1234");
	session.setMaxInactiveInterval(0);//
%>
세션값 저장 했습니다.
<a href="SessionTest.jsp">초기화면으로 가기</a>
</body>
</html>