package diary;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import sun.rmi.server.Dispatcher;


@WebServlet("*.ssg")
public class controller extends HttpServlet {
	private static final long serialVersionUID = 1L;
    public controller() {
        super();
        
    }
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String getRequestURI= request.getRequestURI();
		String getContextPath = request.getContextPath();
		String command = getRequestURI.substring(getContextPath.length()+1);
		System.out.println("��ɾ�"+command);
		if (command.equals("main.ssg")) {
			RequestDispatcher dispatcher = request.getRequestDispatcher("main.jsp");
			dispatcher.forward(request, response);
		}
		
		
		
		
		
		
		
		
		
		
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
