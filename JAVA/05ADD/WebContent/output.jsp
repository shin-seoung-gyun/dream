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
	
	String str1 = new String(request.getParameter("str").getBytes("UTF-8"), "EUC_KR");
	System.out.print(str1);
%>




입력한 값은 <br>
<%=str1 %>
</body>
</html>