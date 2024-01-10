import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int lox = 0;
    int loy = 0;

    int [] x = {0, 1, 0, -1};
    int [] y = {1, 0, -1, 0};
    int turn = 0;

    int n = input.nextInt();

    for(int i = 0; i < n; i++){
      lox += x[turn];
      loy += y[turn];

      if (lox == loy) {
        if(lox > 0)
          turn = 2;
        else
          turn = 0;
      }
      else if (lox == -loy && lox > 0)
        turn = 3;
      else if (loy == -lox + 1 && loy > 0)
        turn = 1;
    }
    System.out.println(lox + " " + loy);
  }
}