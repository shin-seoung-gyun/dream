<%@page import="java.net.URLEncoder"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
String str = "안녕";
str = URLEncoder.encode(str,"utf-8");//한글을 url인코딩해서 보내주면 해결.
%>

<a href = "~~~~~~"></a>

</body>
</html>