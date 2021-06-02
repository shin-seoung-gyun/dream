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
		//모두 여기서 처리됨.
		String requestUri=request.getRequestURI();
		String contextPath = request.getContextPath();
		String command = requestUri.substring(contextPath.length()+1);
		System.out.println("명령어"+command);
		if(command.equals("title.mit")) {
			//디스패쳐로 보내기 title.jsp를 주소표시줄에 노출하지 않음.
			RequestDispatcher dispatcher = request.getRequestDispatcher("title.jsp");
			dispatcher.forward(request, response);
		}else if (command.equals("bye.mit")) {
			response.sendRedirect("bye.jsp");
		}else if (command.equals("write.mit")) {
			DtoMemo dto = new DtoMemo();
			Sv sv = new Sv();
			request.setCharacterEncoding("UTF-8");
			dto.setMemo(request.getParameter("memo"));
			dto.setName(request.getParameter("name"));
			sv.insert(dto);
			response.sendRedirect("next.mit");
		}else if (command.equals("next.mit")) {
			Sv sv = new Sv();
			request.setAttribute("count", sv.count());
			request.setAttribute("best", sv.best());
			int page=1;
			if(request.getParameter("page")!=null) {
				page = Integer.parseInt(request.getParameter("page"));
				if(page<1){
					page=1;
				}
			}
			request.setAttribute("list", sv.list(page));
			RequestDispatcher dispatcher = request.getRequestDispatcher("memo.jsp");
			dispatcher.forward(request, response);
			
		}else if (command.equals("analysis.mit")) {
			Sv sv = new Sv();
			request.setAttribute("analysis", sv.analysis());
			RequestDispatcher dispatcher = request.getRequestDispatcher("analysis.jsp");
			dispatcher.forward(request, response);
		}else if (command.equals("search.mit")) {
			Sv sv = new Sv();
			request.setCharacterEncoding("UTF-8");
			int page=1;//페이지 문제생기면 해결합시다.
			if(request.getParameter("page")!=null) {
				page = Integer.parseInt(request.getParameter("page"));
				if(page<1){
					page=1;
				}
			}
			String search = request.getParameter("search");
			
			request.setAttribute("search", sv.searchList(search, page));
			RequestDispatcher dispatcher = request.getRequestDispatcher("search.jsp");
			dispatcher.forward(request, response);
		}
		
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		doGet(request, response);
	}

}
