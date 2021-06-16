package test;

import java.io.IOException;
import java.util.Random;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/ajax")
public class Servlet01 extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
    public Servlet01() {
        super();
        
    }
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		Random rand = new Random();
		String a = Integer.toString(rand.nextInt(100));
		response.getWriter().append(a);
	}

}
