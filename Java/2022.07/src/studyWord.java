import java.util.Scanner;

public class studyWord {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.next().toUpperCase();
        int [] alp = new int[26];

        for(int i=0; i<word.length(); i++){
            int num = word.charAt(i)-'A';
            alp[num] += 1;
        }

        int max = -1;
        char ans = '?';

        for(int i=0; i<alp.length; i++){
            if(max<alp[i]){
                max = alp[i];
                ans = (char)(i+'A');
            }
            else if(max==alp[i]){
                ans = '?';
            }
        }
        System.out.println(ans);
    }
}
