<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%=request.getParameter("num1") %>����<%=request.getParameter("num2") %>���� ���
�� ���Ѱ��� <%=request.getAttribute("sum") %>
</body>
</html>