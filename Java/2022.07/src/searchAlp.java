import java.util.Scanner;

public class searchAlp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.next();
        int[] alphabet = new int[26];

        for(int i=0; i<alphabet.length; i++){
            alphabet[i]=-1;
        }

        for(int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            if(alphabet[ch-'a'] == -1){ //문자-'a'는 a를 0으로 b를 1로 만들어줌
                alphabet[ch-'a']=i;
            }
        }

        for(int val:alphabet){
            System.out.print(val + " ");
        }
    }
}
