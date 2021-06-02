<%@page import="memo.DtoMemo"%>
<%@page import="java.util.ArrayList"%>
<%@page import="memo.DtoBest"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
[<%=request.getParameter("search")%>] 을(를) 검색한 결과<br>
<%
ArrayList<DtoMemo> list = (ArrayList<DtoMemo>)request.getAttribute("search");
%>

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
String search = request.getParameter("search");
%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href = "search.mit?page=1&search=<%=search%>">검색첫페이지로</a><br><%--url인코딩하면 익스플로러에서도 보낼수 있게됨. 인코딩 디코딩이 헬게이트--%>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href = "search.mit?page=<%=pagenum-1 %>&search=<%=search%>">&lt;&lt;</a>
현재 페이지 번호 <%=pagenum %>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href = "search.mit?page=<%=pagenum+1 %>&search=<%=search%>">>></a><br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href = "next.mit?page=1">기본페이지로</a>
<form action="search.mit" method="post">
메모검색 : <input type="text" required name="search" size="20"><br>
<input type="submit" value="검색">
</form>
</body>
</html>