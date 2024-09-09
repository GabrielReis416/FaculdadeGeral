import java.util.Scanner;

public class Execicio4 {

	public static void main(String[] args) {
		
		 Scanner scanner = new Scanner(System.in);
	        
	        
	        System.out.print("Valor do Salario Minimo: ");
	        int SalarioMin = scanner.nextInt();
	        
	       
	        
	        // Numero de Dependentes
	        
	        
	        System.out.print("Numero de Dependentes:  ");
	        int Depedentes = scanner.nextInt();
	        
	        
	       
	        
	       // Salario do Funcionario
	        
	        System.out.print("Digite Salario do Funcionario:    ");
	        int SalarioFun = scanner.nextInt();
	        
	        
	        
	        
	       // Taxa de Imposto 
	        
	        
	        System.out.print("Taxa de Imposto : ");
	        int TaxaImposto = scanner.nextInt();
	        
	        
	        
	       // Variaveis
	        
	        System.out.println(SalarioMin);
	        System.out.println(Depedentes);
	        System.out.println(SalarioFun);
	        System.out.println(TaxaImposto);
	        
	        
	       // Conta
	        
	        int Alto =  (SalarioMin * 12);
	        int Medio =  (SalarioMin * 5);
	        
	        
	        
	        scanner.close();
	}

}
