import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;

/**
 * @author aweis 
 */

public class LandingPage extends HttpServlet {


    public void doGet(HttpServletRequest request,
                      HttpServletResponse response)
        throws IOException, ServletException
    {
        ResourceBundle rb =
            ResourceBundle.getBundle("LocalStrings",request.getLocale());
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        out.println("<html>");
        out.println("<head>");

	    String title = rb.getString("helloworld.title");

	      out.println("<title>" + title + "</title>");
        out.println("</head>");
        out.println("<body bgcolor=\"white\">");

	// note that all links are created to be relative. this
	// ensures that we can move the web application that this
	// servlet belongs to to a different place in the url
	// tree and not have any harmful side effects.

        // XXX
        // making these absolute till we work out the
        // addition of a PathInfo issue

        out.println("<h1>" + title + "</h1>");
        out.println("<p>Adam Weis</p>");
        out.println("</body>");
        out.println("</html>");
    }
}



