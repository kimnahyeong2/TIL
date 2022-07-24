import java.util.Scanner;

public class repeatChar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testcase = sc.nextInt();

        for(int i=0; i<testcase; i++){
            int rp = sc.nextInt();
            String chr = sc.next();
            String[] aa;

            for(int j=0; j<chr.length(); j++){
                for(int k=0; k<rp; k++){
                    System.out.print(chr.charAt(j));
                }
            }
            System.out.println();
        }
    }
}
