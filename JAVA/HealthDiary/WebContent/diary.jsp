<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<form action="write.do" method="get">
제목<br><input type="text" name="title" ><br><br>
내용 <br><textarea rows=5 cols=50 name="contents"></textarea><br>

<input type="submit" value="등록">
</form>

</body>
</html>