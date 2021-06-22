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

import model.FirstMakeVO;
import model.GroupcodeDAOImpl;
import model.GroupcodeVO;
import model.ProductDAOImpl;
import model.ProductVO;

@WebServlet("*.do")
public class ProductServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	public ProductServlet() {
		super();

	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		PreocessProduct(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		PreocessProduct(request, response);
	}

	protected void PreocessProduct(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		//작성
		//1. 어떤 요청인지 확인
		String uri = request.getRequestURI();
		int lastIndex = uri.lastIndexOf("/");
		String action = uri.substring(lastIndex + 1);
		System.out.println("요청action은:"+action);
		request.setCharacterEncoding("utf-8");
		
		//2. 확인된 요청 처리
		if(action.equals("main.do")){
			//메인화면 요청 이라면 main.jsp를 열어준다.
			response.sendRedirect("main.jsp");
		} else if (action.equals("register.do")){
			//전송된 값 읽기 등록
			ProductVO vo = new ProductVO();
			vo.setCode(request.getParameter("code"));
			vo.setPname(request.getParameter("pname"));
			vo.setCost(Integer.parseInt(request.getParameter("cost")));
			vo.setJnum(Integer.parseInt(request.getParameter("jnum")));
			vo.setPnum(Integer.parseInt(request.getParameter("pnum")));
			vo.setSale(Integer.parseInt(request.getParameter("sale")));
			vo.setGcode(request.getParameter("gcode"));
			//등록							
			ProductDAOImpl dao = new ProductDAOImpl();
			dao.create(vo);
			//다시 등록화면
			response.sendRedirect("productRegister.do");
			
		}else if(action.equals("productRegister.do")) {
			//1. 그룹코드 가져오기
			GroupcodeDAOImpl dao = new GroupcodeDAOImpl();
			dao.list();
			//2. 해당정보 실어서 등록페이지 열기
		
			request.setAttribute("list", dao.list());
			RequestDispatcher dispatcher = request.getRequestDispatcher("productRegister.jsp");
			dispatcher.forward(request, response);
			
		}else if(action.equals("first.do")) {
			ProductDAOImpl dao = new ProductDAOImpl();
			request.setAttribute("list", dao.readFirstMakeList());
			RequestDispatcher dispatcher = request.getRequestDispatcher("first.jsp");
			dispatcher.forward(request, response);
			
		}else if(action.equals("profit.do")) {
			ProductDAOImpl dao = new ProductDAOImpl();
			request.setAttribute("list", dao.readProfitRankList());
			RequestDispatcher dispatcher = request.getRequestDispatcher("profit.jsp");
			dispatcher.forward(request, response);
			
		}else if(action.equals("GroupJnumList.do")) {
			ProductDAOImpl dao = new ProductDAOImpl();
			request.setAttribute("list", dao.readGroupJnumList());
			RequestDispatcher dispatcher = request.getRequestDispatcher("GroupJnumList.jsp");
			dispatcher.forward(request, response);
			
		}else if(action.equals("search.do")) {
			GroupcodeDAOImpl dao = new GroupcodeDAOImpl();
			dao.list();
			//2. 해당정보 실어서 등록페이지 열기
			request.setAttribute("list", dao.list());
			RequestDispatcher dispatcher = request.getRequestDispatcher("search.jsp");
			dispatcher.forward(request, response);
		}else if(action.equals("update.do")) {
			ProductVO vo = new ProductVO();
			vo.setCode(request.getParameter("code"));
			vo.setPname(request.getParameter("pname"));
			vo.setCost(Integer.parseInt(request.getParameter("cost")));
			vo.setJnum(Integer.parseInt(request.getParameter("jnum")));
			vo.setPnum(Integer.parseInt(request.getParameter("pnum")));
			vo.setSale(Integer.parseInt(request.getParameter("sale")));
			vo.setGcode(request.getParameter("gcode"));
			//등록							
			ProductDAOImpl dao = new ProductDAOImpl();
			dao.update(vo);
			response.sendRedirect("search.do");
		}else if(action.equals("find.do")) {
			ProductVO vo = new ProductVO();
			vo.setCode(request.getParameter("code"));
			ProductDAOImpl dao = new ProductDAOImpl();
			request.setAttribute("flist", dao.readOne(vo));
			RequestDispatcher dispatcher = request.getRequestDispatcher("search.do");
			dispatcher.forward(request, response);
		}else if(action.equals("delete.do")) {
			ProductVO vo = new ProductVO();
			vo.setCode(request.getParameter("code"));
			ProductDAOImpl dao = new ProductDAOImpl();
			dao.delete(vo);
			
			response.sendRedirect("search.do");
		}
		
		//3. 해당하는 view열어주기
		
		
		
		
		
		
	}

}
