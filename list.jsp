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
	String start= request.getParameter("startDate");
	String end= request.getParameter("endDate");
	List<DBItem> allList = db.SelectFromDate(start, end);
	int num =1;
	
%>
<h1>��ȸ �Ⱓ</h1> <%=start %> ~ <%=end %>
<table border="1">
<tr>
	<th>ǰ��</th><th>ǰ��</th><th>�ݾ�</th><th>��¥</th>
</tr>
<% for(DBItem temp : allList){%>
<tr>
	<td><%=num++%></td><td><%=temp.item%></td><td><%=temp.money%></td><td><%=temp.date%></td>
</tr>
<%}
%>
</table>

<br>
<a href="index.jsp">�ʱ� ȭ������ ���ư���</a>
</body>
</html>