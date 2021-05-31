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
	session.invalidate();
%>
세션이 초기화 되었습니다.
<a href="SessionTest.jsp">초기화면으로 가기</a>
</body>
</html>