/*
Na Classe MySplit existe dois metodos Split em sobrecarga:

Split(String frase): Recebe uma frase por paramentro e retorna uma lista de char com todas as letras sem os espacos.Exemplo:
  
  Minha Frase de Teste => M,i,n,h,a,F,r,a,s,e,d,e,T,e,s,t,e 

Split(String frase, char delimitador): Recebe uma frase e um delimitador por parametro e retorna uma lista de String das palavras da frase, de acordo com o delimitador, que deve ser um char. Exemplo:
  Minha*Frase*de*Teste => Minha,Frase,de,Teste

obs: Foi usado um ArrayList, para conseguir um array dinamico, ja que nao e possivel saber o tanto de palavras tera no segundo caso ou quantos espacos tera (para subtrair do tamanho da string e criar um array) na frase para o primeiro caso.

*/


import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    MySplit spl = new MySplit();
    System.out.println("\n");

    char teste1[] = spl.Split("Minha Frase de Teste");
    for (int i=0; i<teste1.length; i++){
      System.out.println(teste1[i]);
    }
    System.out.println("");
    String teste2[] = spl.Split("Minha*Frase*de*Teste", '*');
    for (int i=0; i<teste2.length; i++){
      System.out.println("Palavra "+(i+1)+": " + teste2[i]);
    }
  }
}

