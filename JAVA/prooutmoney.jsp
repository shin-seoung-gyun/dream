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
<h1>���� ó�� �Ϸ�</h1><br>
<a href="index.jsp">ó�� ȭ������ ����</a>
</body>
</html>