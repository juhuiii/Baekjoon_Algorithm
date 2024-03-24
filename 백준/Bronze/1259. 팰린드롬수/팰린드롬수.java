import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    while(true){
      char[] num = input.nextLine().toCharArray(); 
      if(num[0] == '0'){
        break;
      }
      boolean palindrome = true;
      for (int i = 0; i < num.length/2; i++){
        if (num[i] != num[num.length -1 - i]){
          palindrome = false;
          break;
        }
      }
      if (palindrome) {
        System.out.println("yes");
      } else {
        System.out.println("no");
      }
    }
  }
}  