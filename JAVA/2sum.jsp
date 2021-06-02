<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%=request.getParameter("num1") %>부터<%=request.getParameter("num2") %>까지 모두
다 더한값은 <%=request.getAttribute("sum") %>
</body>
</html>