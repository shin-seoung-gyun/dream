<%@page import="java.util.Random"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<img alt="space" src="����.png"><br>
<%
Random rand = new Random();
int a = rand.nextInt(100);
%>
<%=a %><br>
<form action="basic.jsp" method="get">
<input type="submit" value="����">

</form>
</body>
</html>