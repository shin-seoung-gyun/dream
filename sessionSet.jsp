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
	session.setAttribute("name", "honggildong");
	session.setAttribute("pw", "1234");
	session.setMaxInactiveInterval(0);//
%>
���ǰ� ���� �߽��ϴ�.
<a href="SessionTest.jsp">�ʱ�ȭ������ ����</a>
</body>
</html>