<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>메모장</title>
</head>
<body>
가장많은 글을 쓴 사람: #(#개글) &nbsp;&nbsp;&nbsp;&nbsp; 총 글개수:<%=request.getAttribute("count") %>
<table border="1">
	<tr>
		<th>순번</th><th>이름</th><th>메모</th><th>작성일</th>
	</tr>
	
	<tr>
		<td>#</td> <td>#</td> <td>#</td> <td>#</td>
	</tr>
	<tr>
		<td>1</td> <td>홍길동</td> <td>안녕하세요</td> <td>2021/05/01 08:10:37</td>
	</tr>
</table>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href = "next.mit">>></a><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="bye.mit">이제 그만</a>
<br><br>
<form action="write.mit" method="post">
이름 : <input type="text" required name="name" size="10"><br>
메모 : <input type="text" required name="memo"size="30"><input type="submit" value="작성" >

</form>
</body>
</html>