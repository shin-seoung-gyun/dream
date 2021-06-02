<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h1>기간 입력</h1>
<br>
<hr>
<br>
<br>
<h3>ex) yy-mm-dd</h3><br>
<form action="list.jsp" method="post">
시작날짜  <input type="date" name="startDate">
끝 날짜  <input type="date" name="endDate"><br>
<br>
<input type="submit" value="확인">

</form>
</body>
</html>