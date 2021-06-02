package controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import model.Sum;

@WebServlet("*.do")
public class Test1 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
  
    public Test1() {
        super();
        
    }
    
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//1. 어떤 요청인지 확인 url확인
		String requestURI=request.getRequestURI();
		System.out.println(requestURI);//test
		String contextPath=request.getContextPath();
		System.out.println(contextPath);//test
		String command=requestURI.substring(contextPath.length());
		System.out.println(command);
		
		if(command.equals("/input.do")) {
			//다른 페이지로 보내기(리다이렉트방식) -새로운 요청 새로운 request영역 (값 보낼수없음)
			response.sendRedirect("input.jsp");
			//다른페이지로 보내기 (디스패쳐 dispatcher)
			//새로운 요청이 아님. 따라서 새로운 request가 아님.(값 보낼수 있음)
//			RequestDispatcher dispatcher = request.getRequestDispatcher("input.jsp");
//			dispatcher.forward(request, response);
			
		} else if(command.equals("/sum.do")) {
			//n~m까지 더해서 결과값 리턴해주는 class
			int sum = Sum.result(request);
			request.setAttribute("sum", sum);
			
			RequestDispatcher dispatcher = request.getRequestDispatcher("sum.jsp");
			dispatcher.forward(request, response);
		}
		
		
		
		
		
		
	}

}
