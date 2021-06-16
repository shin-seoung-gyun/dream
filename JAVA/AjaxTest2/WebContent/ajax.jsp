<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>

</head>
<body>
<img alt="space" src="날씨.png"><br>
랜덤값 <span></span><br>

<input type="submit" value="갱신">

<script src="//code.jquery.com/jquery.min.js"></script>
<script>
$("input").click(function() {
	$.ajax({
		url : "ajax",
		type : "get",
		cache : "false",
		success : function(data) {
			$("span").text(data);
		}
	})
})
</script>
</body>
</html>