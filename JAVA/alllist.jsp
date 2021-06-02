<%@page import="PocketMoney.DBAccess.DBItem"%>
<%@page import="java.util.List"%>
<%@page import="PocketMoney.DBAccess"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<%
	DBAccess db = new DBAccess();
	List<DBItem> allList = db.SelectAllItem();
	int num =1;
	
%>
<table border="1">
<tr>
	<th>품번</th><th>품목</th><th>금액</th><th>날짜</th>
</tr>
<% for(DBItem temp : allList){%>
<tr>
	<td><%=num++%></td><td><%=temp.item%></td><td><%=temp.money%></td><td><%=temp.date%></td>
</tr>
<%}
%>
</table>

<br>
<a href="index.jsp">초기 화면으로 돌아가기</a>


</body>
</html>