import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    String str = new String();
    str = input.nextLine();

    int len = str.length();

    int happy = (len - str.replace(":-)", "").length()) / 3;
    int sad = (len - str.replace(":-(", "").length()) / 3;

    String a = new String("");

    if (happy == 0 && sad == 0){
      a = "none";
    }
    else if(happy > sad){
      a = "happy";
    }

    else if(sad > happy){
      a = "sad";
  }
    else
      a = "unsure";
    System.out.println(a);
  }
}