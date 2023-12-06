import java.util.*;

public class Main{
  public static void main(String[] agrs){
    Scanner input = new Scanner(System.in);

    int n = input.nextInt();
    int l = input.nextInt();

    int[] fruit = new int[n];

    for(int i = 0; i < n; i++){
      fruit[i] = input.nextInt();
    }

    Arrays.sort(fruit);

    for(int i = 0; i < n; i++){
      if(fruit[i] <= l){
        l++;
      }
      else{
        break;
      }
    }
    System.out.println(l);
  }
}