<%-- 
    Document   : apresenta-cliente
    Created on : 10/06/2019, 16:44:25
    Author     : aluno
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Apresentação</title>
    </head>
    <body>
        <h1>Olá <%=request.getParameter("nome")%> seja bem vindo!</h1>
        <h2>Seu email é <%=request.getParameter("email")%>.</h2>
    </body>
</html>
