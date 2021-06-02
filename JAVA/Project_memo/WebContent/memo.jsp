<%@page import="memo.DtoMemo"%>
<%@page import="java.util.ArrayList"%>
<%@page import="memo.DtoBest"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>메모장</title>
</head>
<body>
<%
DtoBest best = (DtoBest)request.getAttribute("best");
ArrayList<DtoMemo> list = (ArrayList<DtoMemo>)request.getAttribute("list");
%>



가장많은 글을 쓴 사람: <%=best.getName() %>(<%=best.getCount() %>개글) &nbsp;&nbsp;&nbsp;&nbsp; 총 글개수:<%=request.getAttribute("count") %>
<table border="1">
	<tr>
		<th>순번</th><th>이름</th><th>메모</th><th>작성일</th>
	</tr>
	<%for(DtoMemo temp : list){%>
	<tr>
		<td><%=temp.getNo() %></td> <td><%=temp.getName() %></td> <td><%=temp.getMemo() %></td> <td><%=temp.getTime() %></td>
	</tr>
	<%}%>
</table>
<%
String strPage = request.getParameter("page");
int pagenum=1;
if(strPage!=null){
	pagenum=Integer.parseInt(strPage);
	if(pagenum<1){
		pagenum=1;
	}
}

%>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href = "next.mit?page=1">첫페이지로</a><br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href = "next.mit?page=<%=pagenum-1 %>">&lt;&lt;</a>
현재 페이지 번호 <%=pagenum %>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href = "next.mit?page=<%=pagenum+1 %>">>></a><br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="bye.mit">이제 그만</a>
<form action="search.mit" method="post">
메모검색 : <input type="text" required name="search" size="20"><br>
<input type="submit" value="검색" >
</form>
<br><br>
<form action="write.mit" method="post">
이름 : <input type="text" required name="name" size="10"><br>
메모 : <input type="text" required name="memo"size="30"><input type="submit" value="작성" >
</form>
<br>
<br>
<a href="analysis.mit" target="_blank">분석</a>
</body>
</html>


