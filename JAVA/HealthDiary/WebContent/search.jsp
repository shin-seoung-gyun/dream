<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>일기검색</h1>

<c:if test="${list == null }">
<form action="search.do" >
날짜 입력 <input type="date" name="date">
<input type="submit" value="검색">

</form>

</c:if>


<c:if test="${list != null }">
<table border="1">
<tr>
	<th>제목</th><th>날짜</th>
</tr>
<c:forEach items="${list}" var="temp">
<tr>
	<td>${ temp.getTitle() }</td><td>${temp.getDate()}</td>
</tr>
	</c:forEach>

</table>
<form action="search2.do" >
정확한 날짜 입력 <input type="text" name="date">
<input type="submit" value="검색">
</form>
</c:if>



</body>
</html>