import java.util.ArrayList;

class MySplit {
  public char[] Split(String frase) {

    ArrayList lista = new ArrayList(); //criando um array dinamico

    //Pegando cada letra da frase 
    for(int i=0; i<frase.length(); i++){
      if(frase.charAt(i) != ' '){
        lista.add(frase.charAt(i));
      }
    }

    //Convertendo o ArrayList, para uma lista de char
    char result[] = new char[lista.size()];
    for (int i = 0; i<lista.size(); i++){
      result[i] = (Character)lista.get(i); 
    }
    return result;
  }

  public String[] Split(String frase, char delimitador) {
 
    String palavra = "";
    ArrayList lista = new ArrayList();

    for(int i=0; i<frase.length(); i++){//rodar letra a letra
      if(frase.charAt(i) == delimitador){ // Se a letra atual == delimitador entao adicionar a palavra na lista
        if(palavra !=""){//nao adicionar palavras vazias
          lista.add(palavra);
          palavra = "";
        }
      }else if(i == frase.length()-1){ //se e a ultima letra adiciona ela na palavra e a palavra na lista
        palavra = palavra + frase.charAt(i);
        lista.add(palavra);
      }
      else{ // se nao, adiciona a letra na palavra apenas
        palavra = palavra + frase.charAt(i);
      }
    }

    //Convertendo o ArrayList, para uma lisa de String
    String result[] = new String[lista.size()];
    for (int i = 0; i<lista.size(); i++){
      result[i] = ""+lista.get(i); 
    }
    return result; //retorna uma lista de String
  }
}
