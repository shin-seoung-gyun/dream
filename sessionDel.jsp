<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
세션의 pw를 삭제합니다.
<%
	session.removeAttribute("pw");
%>
<a href="SessionTest.jsp">초기화면으로 가기</a>
</body>
</html>