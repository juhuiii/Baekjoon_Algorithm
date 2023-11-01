import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    String str = input.next();
    String array [] = str.split("");

    int t = input.nextInt();

    for(int i = 0; i < t; i++){
      int a = input.nextInt();
      int b = input.nextInt();
      String temp = "";

      temp = array[a];
      array[a] = array[b];
      array[b] = temp;
    }
    

    for(int i = 0; i < array.length; i++){
      System.out.print(array[i]);
    }
  }
} 