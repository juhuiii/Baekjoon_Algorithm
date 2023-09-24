import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int test = input.nextInt();
    
    for(int i = 1; i <= test; i++){
      int n = input.nextInt();
      int count1 = 0;
      int count2 = 0;
      
      for(int j = 1; j <= n; j++){
        String player1 = input.next();
        String player2 = input.next();
        
        if((player1.equals("R") && player2.equals("P")) || (player1.equals("S") && player2.equals("R")) || (player1.equals("P") && player2.equals("S"))){
          count2 ++;
        }
        if((player1.equals("R") && player2.equals("S")) || (player1.equals("S") && player2.equals("P")) || (player1.equals("P") && player2.equals("R"))){
          count1++;
        }
      }
      
      if(count1 == count2){
        System.out.println("TIE");
      }
      else if(count1 > count2){
        System.out.println("Player 1");
      }
      else{
        System.out.println("Player 2");
      }
    }
    
  }
}