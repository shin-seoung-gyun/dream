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
		//1. � ��û���� Ȯ�� urlȮ��
		String requestURI=request.getRequestURI();
		System.out.println(requestURI);//test
		String contextPath=request.getContextPath();
		System.out.println(contextPath);//test
		String command=requestURI.substring(contextPath.length());
		System.out.println(command);
		
		if(command.equals("/input.do")) {
			//�ٸ� �������� ������(�����̷�Ʈ���) -���ο� ��û ���ο� request���� (�� ����������)
			response.sendRedirect("input.jsp");
			//�ٸ��������� ������ (������ dispatcher)
			//���ο� ��û�� �ƴ�. ���� ���ο� request�� �ƴ�.(�� ������ ����)
//			RequestDispatcher dispatcher = request.getRequestDispatcher("input.jsp");
//			dispatcher.forward(request, response);
			
		} else if(command.equals("/sum.do")) {
			//n~m���� ���ؼ� ����� �������ִ� class
			int sum = Sum.result(request);
			request.setAttribute("sum", sum);
			
			RequestDispatcher dispatcher = request.getRequestDispatcher("sum.jsp");
			dispatcher.forward(request, response);
		}
		
		
		
		
		
		
	}

}
