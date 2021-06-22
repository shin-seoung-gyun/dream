<%@page import="model.GroupcodeVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>제품입력</title>
</head>
<body>
<h1>생산관리등록화면</h1>

<fieldset>
<legend>생산관리등록화면</legend>
<form action="register.do" method="get">
제품코드<input type="text" name="code" ><br>
제품명<input type="text" name="pname"><br>
제품원가<input type="text" name="cost"><br>
재고수량<input type="text" name="jnum"><br>
목표수량<input type="text" name="pnum"><br>
출고가<input type="text" name="sale"><br>
그룹이름<select name = "gcode">
<c:forEach items="${list}" var="temp">
		<option value="${temp.getGcode()}">${temp.getGname()}</option>
		
</c:forEach>
</select>
<br>
<input type="submit" value="등록">
<input type="button" value="메인화면" onclick="location.href='main.do'">

</form>

</fieldset>



</body>
</html>