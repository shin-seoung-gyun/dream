<%@page import="model.FirstMakeVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>  
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>우선 생산 품목</h1>

<table border="1">
<tr>
	<th>품목</th><th>필요 생산 재고</th>
</tr>
<c:forEach items="${list}" var="temp">
<tr>
	<td>${ temp.getPname() }</td><td>${temp.getJnum()}</td>
</tr>
	</c:forEach>

</table>
















</body>
</html>