<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>

</head>
<body>
<img alt="space" src="����.png"><br>
������ <span></span><br>

<input type="submit" value="����">

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