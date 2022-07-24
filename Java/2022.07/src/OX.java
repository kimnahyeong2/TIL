import java.util.Scanner;

public class OX {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        
        String [] ox = new String[n];
        int [] result = new int[n];

        for(int i=0; i<ox.length; i++){
            ox[i] = scan.next();
            char[] ox_array = new char[ox[i].length()];
            int score = 0;
            for(int j=0; j<ox_array.length; j++){
                ox_array[j] = (ox[i].charAt(j));
                if(ox_array[0]=='O'){
                    score = 1;
                }
            }
            int cnt = 1;
            for(int k=1; k<ox_array.length; k++){
                if(ox_array[k]==ox_array[k-1] && ox_array[k]=='O'){
                    cnt += 1;
                    score += cnt;
                }
                else if(ox_array[k] != ox_array[k-1] && ox_array[k]=='O'){
                    cnt = 1;
                    score += cnt;
                }
                else{
                    cnt = 1;
                }
            }
            result[i] = score;
        }

        for(int i=0; i<n; i++){
            System.out.println(result[i]);
        }

    }
}
    