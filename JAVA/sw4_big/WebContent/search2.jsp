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
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
</head>
<body>
	<h1>생산관리 조회 수정 화면</h1>
	<fieldset>
		<legend>생산관리 조회 수정 화면</legend>


		<form action="find.do" method="get">
			제품코드<input type="text" name="code" value="${flist.getCode()}"><br>
			제품명<input type="text" name="pname" value="${flist.getPname()}"><br>
			제품원가<input type="text" name="cost" value="${flist.getCost()}"><br>
			재고수량<input type="text" name="jnum" value="${flist.getJnum()}"><br>
			목표수량<input type="text" name="pnum" value="${flist.getPnum()}"><br>
			출고가<input type="text" name="sale" value="${flist.getSale()}"><br>
			그룹이름<select name="gcode">
				<c:forEach items="${list}" var="temp">
					<option
						<c:if test="${flist.getGcode() eq temp.getGcode()}">
						selected
						</c:if>
						value="${temp.getGcode()}">${temp.getGname()}</option>
				</c:forEach>
			</select> <br> <input type="submit" value="조회">
			<!-- 		<input type="submit" value="수정" formaction="update.do"> -->
			<!-- 		<input type="submit" value="삭제" formaction="delete.do">  -->
			<input type="submit" value="수정" id="modify"> <input
				type="buttom" value="삭제" id="delete"> <input type="button"
				value="메인화면" onclick="location.href='main.do'">
		</form>

	</fieldset>

	<script>
//jquery
//문서가 다 로딩된후 스크립트를 실행시켜라 스크립트 기본 사용법이니 기억해두자
$(document).ready(function(){
	console.log("${product}");
	//alert("안내창으로 출력")
	var product = "${product}";
	$("#modify").click(function(e){
		e.preventDefault();//이벤트 처리를 무시 알아둘것.(버튼이나 해당 아이디 태그가 가지고 있는 기본 이벤트를 무시한다.)
		if(product===""){
		alter("조회후 수정해주세요");
		}else{
			$("form").attr("action", "update.do");
			$("form").submit();
		}
})
	$("#delete").click(function(){
		if(product===""){
		alter("조회후 삭제해주세요");
		}else{
			$("form").attr("action", "delete.do");
			$("form").submit();
		}
})
})

</script>





</body>
</html>