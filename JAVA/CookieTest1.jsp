<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
��Ű�� �׽�Ʈ �մϴ�.
1.��Ű�� ����
<%
	Cookie cookie = new Cookie("name","honggildong");//��Ű�� �̸��� ���� �����Ҽ��ִ�.
	cookie.setMaxAge(600);//�ʸ� �Է��Ͽ� ����Ⱓ�� �����Ҽ� ����.
	response.addCookie(cookie);//�������� ��Ű�� ����� Ŭ���̾�Ʈ�� ����.
%>
<a href = "CookieTest2.jsp">��Ű�� �ҷ�����</a>
</body>
</html>