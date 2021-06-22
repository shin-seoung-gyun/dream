<%@page import="model.ProfitRankVo"%>
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
<h1>재고 완판 수익</h1>

<table border="1">
<tr>
	<th>품목</th><th>재고 완판 수익</th>
</tr>
<c:forEach items="${list}" var="temp">
<tr>
	<td>${ temp.getPname() }</td><td>${temp.getProfit()}</td>
</tr>
	</c:forEach>

</table>

</body>
</html>