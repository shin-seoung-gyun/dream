package time;

import java.io.IOException;
import java.util.Calendar;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/GetServer")
public class TimeServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
    public TimeServlet() {
        super();
       
    }


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//���� ��(second)��  text�� ����.
		//���� �ý����� �� �޾ƿ���
		Calendar c = Calendar.getInstance();
		response.getWriter().append(Integer.toString(c.get(Calendar.SECOND)));
	}

}










