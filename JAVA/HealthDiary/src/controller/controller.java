package controller;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import diary.DiaryDAOImpl;
import diary.DiaryListVO;

@WebServlet("*.do")
public class controller extends HttpServlet {
	private static final long serialVersionUID = 1L;

	public controller() {
		super();

	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doWork(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doWork(request, response);
	}

	protected void doWork(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String uri = request.getRequestURI();
		int lastIndex = uri.lastIndexOf("/");
		String action = uri.substring(lastIndex + 1);
		System.out.println("요청action은:" + action);
		request.setCharacterEncoding("utf-8");

		if (action.equals("write.do")) {// 일기 등록
			// 전송된 값 읽기 등록
			DiaryListVO vo = new DiaryListVO();
			vo.setTitle(request.getParameter("title"));
			vo.setDate(request.getParameter("date"));
			vo.setContents(request.getParameter("contents"));
			// 등록
			DiaryDAOImpl dd = new DiaryDAOImpl();
			dd.insert(vo);
			// 다시 등록화면
			response.sendRedirect("diary.jsp");
		}else if (action.equals("search.do")) {// 날자로 일기 리스트 가져오기
			DiaryDAOImpl dd = new DiaryDAOImpl();
			DiaryListVO vo = new DiaryListVO();
			vo.setDate(request.getParameter("date"));
			request.setAttribute("list", dd.searchDate(vo));
			RequestDispatcher dispatcher = request.getRequestDispatcher("search.jsp");
			dispatcher.forward(request, response);
			
		}else if (action.equals("search2.do")) {//날자 시간으로 내용까지 가져오기
			DiaryDAOImpl dd = new DiaryDAOImpl();
			DiaryListVO vo = new DiaryListVO();
			vo.setDate(request.getParameter("date"));
			request.setAttribute("list", dd.searchDateTime(vo));
			RequestDispatcher dispatcher = request.getRequestDispatcher("search2.jsp");
			dispatcher.forward(request, response);
			
		}else if (action.equals("delete.do")) {// 삭제하기
			DiaryDAOImpl dd = new DiaryDAOImpl();
			DiaryListVO vo = new DiaryListVO();
			vo.setDate(request.getParameter("date"));
			dd.delete(vo);
			RequestDispatcher dispatcher = request.getRequestDispatcher("search.jsp");
			dispatcher.forward(request, response);
		}else if (action.equals("update.do")) {// 수정하는 매서드
			DiaryListVO vo = new DiaryListVO();
			vo.setTitle(request.getParameter("title"));
			vo.setDate(request.getParameter("date"));
			vo.setContents(request.getParameter("contents"));
			System.out.println(vo.getDate());
			// 등록
			DiaryDAOImpl dd = new DiaryDAOImpl();
			dd.update(vo);
			RequestDispatcher dispatcher = request.getRequestDispatcher("search2.do");
			dispatcher.forward(request, response);
			
		}
			
			
			
			
			
		
		
		
		
		
		
		
		
		
		
		
		

	}

}
