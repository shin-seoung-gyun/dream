<%@page import="PocketMoney.DBAccess"%>
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
	request.setCharacterEncoding("EUC-KR");
	String item = request.getParameter("item");
	String money = request.getParameter("money");
	DBAccess db = new DBAccess();
	db.insertRow(item,"-"+money);
%>
<h1>지출 처리 완료</h1><br>
<a href="index.jsp">처음 화면으로 가기</a>
</body>
</html>