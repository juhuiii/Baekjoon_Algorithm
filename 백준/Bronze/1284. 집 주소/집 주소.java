import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    
    while(true){
      int count = 0;
      String num = input.next();

      if(num.equals("0")){
        break;
      }
      for(int i = 0; i < num.length(); i++){
        String a = num.substring(i, i + 1);
  
        if(a.equals("1")){
          count += 3;
        }
        else if(a.equals("0")){
          count += 5;
        }
        else{
          count += 4;
        }
      }
      System.out.println(count + 1);
    }
  }
}