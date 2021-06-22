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
<h1>그룹별 재고수량 </h1>

<table border="1">
<tr>
	<th>그룹명</th><th>재고 수</th>
</tr>
<c:forEach items="${list}" var="temp">
<tr>
	<td>${temp.getGcode()}</td><td>${temp.getJnum()}</td>
</tr>
	</c:forEach>

</table>

</body>
</html>