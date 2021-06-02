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
	int a = Integer.parseInt( request.getParameter("num1"));
	int b = Integer.parseInt(request.getParameter("num2")) ;
	int sum = 0;
	for (int i =a; i<=b;i++){
		sum +=i;
	}


%>
<%=a %>부터 <%=b %>까지 더한 값은 <%=sum %>입니다
</body>
</html>