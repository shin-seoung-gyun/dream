package memo;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("*.mit")
public class Controller extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
 
    public Controller() {
        super();
     
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//��� ���⼭ ó����.
		String requestUri=request.getRequestURI();
		String contextPath = request.getContextPath();
		String command = requestUri.substring(contextPath.length()+1);
		System.out.println("��ɾ�"+command);
		if(command.equals("title.mit")) {
			//�����ķ� ������ title.jsp�� �ּ�ǥ���ٿ� �������� ����.
			RequestDispatcher dispatcher = request.getRequestDispatcher("title.jsp");
			dispatcher.forward(request, response);
		}else 	if(command.equals("memo.mit")) {
			Sv sv = new Sv();
			request.setAttribute("count", sv.count());
			RequestDispatcher dispatcher = request.getRequestDispatcher("memo.jsp");
			dispatcher.forward(request, response);
		}
		
		
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		doGet(request, response);
	}

}
