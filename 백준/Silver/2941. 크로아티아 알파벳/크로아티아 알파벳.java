import java.util.*;
public class Main{
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String str = input.next();

    String [] c = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    
    for(int i = 0; i < c.length; i++){
      str = str.replace(c[i], "a");
    }
    System.out.println(str.length());
  } 
}