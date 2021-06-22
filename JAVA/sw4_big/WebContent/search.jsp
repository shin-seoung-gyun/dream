<%@page import="model.GroupcodeVO"%>
<%@page import="java.util.ArrayList"%>
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
	<h1>생산관리 조회 수정 화면</h1>
	<fieldset>
		<legend>생산관리 조회 수정 화면</legend>
		<c:if test="${flist == null}">
			<form action="find.do" method="get">
				제품코드1<input type="text" name="code"><br> 
				제품명<input	type="text" name="pname"><br> 
				제품원가<input type="text" name="cost"><br> 
				재고수량<input type="text" name="jnum"><br>
				목표수량<input type="text" name="pnum"><br> 
				출고가<input	type="text" name="sale"><br> 
				그룹이름<select name="gcode">
					<c:forEach items="${list}" var="temp">
						<option value="${temp.getGcode()}">${temp.getGname()}</option>
					</c:forEach>
				</select>
		</c:if>
		<c:if test="${flist != null}">
			<form action="find.do" method="get">
				제품코드<input type="text" name="code" value="${flist.getCode()}"><br>
				제품명<input type="text" name="pname" value="${flist.getPname()}"><br>
				제품원가<input type="text" name="cost" value="${flist.getCost()}"><br>
				재고수량<input type="text" name="jnum" value="${flist.getJnum()}"><br>
				목표수량<input type="text" name="pnum" value="${flist.getPnum()}"><br>
				출고가<input type="text" name="sale" value="${flist.getSale()}"><br>
				그룹이름<select name="gcode" >
					<c:forEach items="${list}" var="temp" >
						<option 
						<c:if test="${flist.getGcode() eq temp.getGcode()}">
						selected
						</c:if>
						value="${temp.getGcode()}">${temp.getGname()}</option>
					</c:forEach>
				</select>
		</c:if>


		<input type="submit" value="조회">
		<input type="submit" value="수정" formaction="update.do">
		<input type="submit" value="삭제" formaction="delete.do"> 
		<input type="button" value="메인화면" onclick="location.href='main.do'">
		</form>
	</fieldset>
</body>
</html>