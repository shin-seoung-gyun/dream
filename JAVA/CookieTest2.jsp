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
	String cookie=request.getHeader("Cookie");
	String name="";
	String value="";
	if(cookie!=null){
		Cookie cookies[]=request.getCookies();
		for(Cookie temp:cookies){
			name += temp.getName()+"\n\n";
			value += temp.getValue()+"\n\n";
		}
	}
%>
��Ű �̸��� <%=name %><br>
 ��Ű ���� <%=value %>
</body>
</html>