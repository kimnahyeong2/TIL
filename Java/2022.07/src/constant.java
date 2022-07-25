import java.util.Scanner;

public class constant {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        a = (((a%100)%10)*100) + (((a%100)/10)*10) + (a/100);
        b = (((b%100)%10)*100) + (((b%100)/10)*10) + (b/100);

        if(a>b){
            System.out.println(a);
        }
        else{
            System.out.println(b);
        }
    }
}
