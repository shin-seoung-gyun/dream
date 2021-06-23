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
<h1>일기내용</h1>
<table border="1">
<tr>
	<th>제목</th><th>내용</th><th>날짜</th>
</tr>

<tr>
	<td>${ list.getTitle() }</td><td>${ list.getContents() }</td><td>${list.getDate()}</td>
</tr>
</table>
<form action="delete.do">
<input type="hidden" name="date" value="${list.getDate()}">
<input type="submit" value="삭제" >
</form>
<form action="update.do">
<input type="hidden" name="date" value="${list.getDate()}">
제목<br> <input type="text" name="title"><br>
내용<br> <textarea rows=5 cols=50 name="contents"></textarea><br>
<input type="submit" value="수정" >
</form>
</body>
</html>