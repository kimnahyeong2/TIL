import java.util.Scanner;

public class aNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(n(sc.nextInt()));
        sc.close();
    }

    public static int n(int number){
        int cnt = 0;
        if(number<100){
            return number;
        }
        else{
            cnt = 99;
            for(int i=100; i<=number; i++){
                int hun = i/100;
                int ten = (i/10) % 10;
                int one = i % 10;
                if((hun-ten) == (ten-one)){
                    cnt += 1;
                }
            }
            return cnt;
        }
    }
}
