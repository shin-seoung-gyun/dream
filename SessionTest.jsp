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
	String name="세션id 없음";
	if(session.getAttribute("name")!=null){
	name=(String)session.getAttribute("name");
	}
	
	String pw="세션pw 없음";
	if(session.getAttribute("pw")!=null){
	pw=(String)session.getAttribute("pw");
	}
%>

세션값 보기 id는<%=name %> pw는 <%=pw %><br>

<a href="sessionSet.jsp">1.세션값 저장</a><br>

<a href="sessionDel.jsp">2.세션값 삭제</a><br>

<a href="sessionInit.jsp">3.세션값 초기화</a><br>
</body>
</html>