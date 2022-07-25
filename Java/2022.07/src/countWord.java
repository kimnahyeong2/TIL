import java.util.Scanner;

public class countWord {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String a = sc.nextLine();
        a = a.strip();
        String [] word = a.split(" ");
        if(word[0]==""){
            System.out.println("0");
        }
        else{
            System.out.println(word.length);
        }
    }
}
