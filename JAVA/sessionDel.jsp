<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
������ pw�� �����մϴ�.
<%
	session.removeAttribute("pw");
%>
<a href="SessionTest.jsp">�ʱ�ȭ������ ����</a>
</body>
</html>