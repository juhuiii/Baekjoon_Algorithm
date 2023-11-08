  import java.util.*;

  public class Main{
    public static void main(String[] args){
      Scanner input = new Scanner(System.in);
      
      while(input.hasNext()){
        double n = input.nextDouble();
        double b = input.nextDouble();
        double m = input.nextDouble();
        int count = 0;

        while (n <= m){
          n += n * (b /100);
          count++;
        }
        System.out.println(count);
    }
  } 
}
