import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        int N = Integer.parseInt(bufferedReader.readLine());

        makeSiteSign(N);
    }

    private static void makeSiteSign(int N) {
        if (N == 1) {
            System.out.println("*");
        } else {

            for (int i = 0; i < N; i++) {     //세로 N줄
                System.out.print("*"); 

                if (i == 0) {
                    for (int j = 0; j < N - 2; j++)
                        System.out.print("*");
                } else if (i == N - 1) {
                    for (int j = 0; j < N - 2; j++)
                        System.out.print("*");
                } else {
                    for (int j = 0; j < N - 2; j++) {
                        /*
                         * i == 1 -> j = 0, 12
                         * i == 2 -> j = 1, 11
                         * i == 3 -> j = 2, 10
                         * */
                        if (j == i - 1 || j == N - (i + 2)) System.out.print("*");
                        else System.out.print(" ");

                    }
                }
                System.out.println("*");  //가로 줄에서 마지막 * 출력
            } //end - for문
        } //end - else문
    }
}