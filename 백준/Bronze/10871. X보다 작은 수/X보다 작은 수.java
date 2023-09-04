import java.util.Scanner;
 
public class Main {
        public static void main(String[] args) {
                Scanner in = new Scanner(System.in);
 
                int a = in.nextInt();
                int b = in.nextInt();
                int arr[] = new int[a];
        
                for (int i = 0; i < a; i++) {
                        arr[i] = in.nextInt();
                }
 
                in.close();
        
                for (int i = 0; i < a; i++) {
                        if (arr[i] < b) {
                                System.out.print(arr[i] + " ");
                        }
                }
        }
}