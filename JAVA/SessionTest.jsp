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
	String name="����id ����";
	if(session.getAttribute("name")!=null){
	name=(String)session.getAttribute("name");
	}
	
	String pw="����pw ����";
	if(session.getAttribute("pw")!=null){
	pw=(String)session.getAttribute("pw");
	}
%>

���ǰ� ���� id��<%=name %> pw�� <%=pw %><br>

<a href="sessionSet.jsp">1.���ǰ� ����</a><br>

<a href="sessionDel.jsp">2.���ǰ� ����</a><br>

<a href="sessionInit.jsp">3.���ǰ� �ʱ�ȭ</a><br>
</body>
</html>