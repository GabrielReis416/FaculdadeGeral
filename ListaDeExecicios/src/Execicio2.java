
import java.util.*;

public class Execicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        
        System.out.print("Digite a quantidade de numeros: ");
        int n = scanner.nextInt();
        int[] array = new int[n];
        
        System.out.println("Digite os numeros:");
        for (int i = 0; i < n; i++) {
            array[i] = scanner.nextInt();
        }
        
        
        int sum = 0;
        for (int num : array) {
            sum += num;
        }
        System.out.println("A soma de todos os elementos é: " + sum);
        
        
        int max = array[0];
        int min = array[0];
        
        for (int num : array) {
            if (num > max) max = num;
            if (num < min) min = num;
        }
        
        System.out.println("O maior valor é: " + max);
        System.out.println("O menor valor é: " + min);
        
        
        double average = (double) sum / n;
        System.out.println("A média dos elementos é: " + average);
        
        
        Arrays.sort(array);
        double median;
        if (n % 2 == 0) {
            median = (array[n / 2 - 1] + array[n / 2]) / 2.0;
        } else {
            median = array[n / 2];
        }
        System.out.println("A mediana dos elementos é: " + median);
        
        
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : array) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        
        int maxCount = Collections.max(frequencyMap.values());
        List<Integer> modes = new ArrayList<>();
        
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            if (entry.getValue() == maxCount) {
                modes.add(entry.getKey());
            }
        }
        
        System.out.print("A(s) moda(s) é(são): ");
        for (int mode : modes) {
            System.out.print(mode + " ");
        }
        System.out.println();
        
        scanner.close();
    }
}


