import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static int T;
    static Scanner sc = new Scanner(System.in);
    static List<String> numbers = new ArrayList<>();

    public static void main(String[] args) {
        T = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < T; i++) {
            String temp;
            temp = sc.nextLine();
            numbers.add(temp);
        }

        for (int i = 0; i < T; i++) {
            if (isValid(numbers.get(i)))
                System.out.println("T");
            else
                System.out.println("F");
        }
    }

    static boolean isValid(String number) {
        int cnt = 1;

        for (int i = number.length() - 1; i >= 0; i--) {
            if (cnt % 2 != 0) {
                // 추후 모든 자리의 수를 더하기 위해 숫자로 저장
                char[] tempNumber = number.toCharArray();
                tempNumber[i] -= '0';
                number = String.valueOf(tempNumber);

                cnt++;
                continue;
            }

            int twiceNum = (number.charAt(i) - '0') * 2;
            if (twiceNum >= 10) {
                // 2배로 만든 수는 무조건 10 이상 18 이하이므로 1 + (수 - 10)으로 계산
                twiceNum = 1 + (twiceNum - 10);
            }

            // 추후 모든 자리의 수를 더하기 위해 숫자로 저장
            char[] tempNumber = number.toCharArray();
            tempNumber[i] = (char)twiceNum;
            number = String.valueOf(tempNumber);

            cnt++;
        }

        int k = 0;

        for (int i = 0; i < number.length(); i++)
            k += number.charAt(i);

        return (k % 10 == 0) ? true : false;
    }
}