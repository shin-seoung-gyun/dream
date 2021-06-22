<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>생산관리시스템</title>
<style >
input{
	width: 200px;
	height : 50px;
	background: rgb(242,240,202); 
}



</style>
</head>
<body>
<h1>생산관리 시스템</h1>
<fieldset>
<legend>생산관리 메인메뉴</legend>
<input type="button" value="제품입력" onclick="location.href='productRegister.do'">
<input type="button" value="제품조회" onclick="location.href='search.do'">
<input type="button" value="우선생산제품" onclick="location.href='first.do'">
<input type="button" value="이익순위" onclick="location.href='profit.do'">
<input type="button" value="그룹별재고수량" onclick="location.href='GroupJnumList.do'">



</fieldset>


</body>
</html>