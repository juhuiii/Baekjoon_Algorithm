import java.util.*;

public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int n = input.nextInt();
    int home = 0;
    int array [] = new int[100];

    for(int i = 0; i < n; i++){
      int customer = input.nextInt();

      if(array[customer - 1] == 0){ 
        array[customer - 1] ++;
      }
      else {
        home ++;
      }

    }
    System.out.println(home);
  }
} 