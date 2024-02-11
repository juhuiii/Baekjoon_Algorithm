import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    int[] num = new int[3];

    for(int i = 0; i < 3; i++){
      num[i] = input.nextInt();
    }
    if (num[0] % 2 == 0 && num[1] % 2 == 0 && num[2] % 2 == 0){
      System.out.println(num[0] * num[1] * num[2]);
    }
    else {
      int odd = 1;
      if( num[0] % 2 == 1){
        odd *= num[0];
      }
      if( num[1] % 2 == 1){
        odd *= num[1];
      }
      if( num[2] % 2 == 1){
        odd *= num[2];
      }
      System.out.println(odd);
    }
  }
}
