function submit_login(){
    if (document.form1.cpf.value == ""){
        alert("Campo cpf obrigatório");
        return false;
    }else if (document.form1.senha.value == ""){
        alert("Campo senha obrigatório");
        return false;
    }else if (document.form1.senha.value == "senha" && document.form1.cpf.value != "123456789"){
        confirm("Login efetuado com Sucesso!");
        return false;
    } else {
        alert("Login e/ou senha incorretos!");
        return false;
    }
}

