import java.util.Scanner;

public class Execicio3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        
        System.out.print("Digite uma palavra: ");
        String input = scanner.nextLine();
        
        
        char[] wordArray = input.toCharArray();
        
        
        boolean isPalindrome = true;
        int left = 0;
        int right = wordArray.length - 1;
        
        while (left < right) {
            if (wordArray[left] != wordArray[right]) {
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }
        
        if (isPalindrome) {
            System.out.println("A palavra \"" + input + "\" é um palíndromo.");
        } else {
            System.out.println("A palavra \"" + input + "\" não é um palíndromo.");
        }
        
        scanner.close();
    }
}