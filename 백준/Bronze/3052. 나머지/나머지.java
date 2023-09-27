import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int [] nums = new int [10];
    boolean b;
    int result = 0 ;

    for(int i = 0; i < 10; i++){
      nums[i] = input.nextInt() % 42 ;
    }

    for(int i = 0; i < 10; i++){
      b = false ; 
      for(int j = i + 1; j < 10; j++){
        if (nums[i] == nums[j]) {
          b = true ;
          break;
        } 
      }
      if (b == false){
        result ++;
      }
    }
    System.out.println(result);
  }
}