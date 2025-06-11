fun main() {
    val distancias = mutableListOf<Double>()
    val missoes = mutableListOf<String>()
    var continuar: String

    // Laço de repetição 
    do {
        println("===== NOVA MISSÃO =====")
        print("Nome do astronauta comandante da missão: ")
        val comandante = readLine() ?: ""

        print("Distância da Terra até Marte (em milhões de km): ")
        val distancia = readLine()?.toDoubleOrNull() ?: 0.0

        print("Quantidade de tripulantes na nave: ")
        val numeroTripulantes = readLine()?.toIntOrNull() ?: 0

        print("Consumo de combustível por milhão de km (em litros): ")
        val consumoCombustivel = readLine()?.toDoubleOrNull() ?: 0.0

        print("Custo do litro de combustível (em reais): ")
        val custoLitro = readLine()?.toDoubleOrNull() ?: 0.0

        print("Quantidade média de refeições por dia por tripulante: ")
        val mediaRefeicoes = readLine()?.toIntOrNull() ?: 0

        print("Duração estimada da viagem (em dias): ")
        val duracao = readLine()?.toDoubleOrNull() ?: 0.0

        val totalCombustivel = distancia * consumoCombustivel
        val custoTotalCombustivel = totalCombustivel * custoLitro
        val totalRefeicoes = numeroTripulantes * mediaRefeicoes * duracao

        // Printar Resultados

        println("\n===== RELATÓRIO DA MISSÃO =====")
        println("Comandante: $comandante")
        println("Distância: $distancia milhões de km")
        println("Tripulantes: $numeroTripulantes")
        println("Total de combustível: $totalCombustivel litros")

        // Condicional 

        if (totalCombustivel > 20000) {
            println("Alerta: essa missão pode estar além da capacidade atual de combustível!")
        } else {
            println("Missão dentro dos limites de combustível.")
        }

        println("Custo total do combustível: R$ $custoTotalCombustivel")
        println("Total de refeições: $totalRefeicoes")

        when {
            totalRefeicoes < 1000 -> println("Aviso: a quantidade de refeições parece insuficiente para a missão.")
            totalRefeicoes in 1000.0..3000.0 -> println("✅ Quantidade de refeições adequada.")
            totalRefeicoes > 3000 -> println("Refeições em excesso: considere reduzir para otimizar o espaço.")
        }

        // Leitura dos módulos da estação espacial
        print("\nQuantidade de módulos da estação espacial: ")
        val qtdModulos = readLine()?.toIntOrNull() ?: 0
        val temperaturasModulos = mutableListOf<Double>()

        for (i in 1..qtdModulos) {
            print("Temperatura do módulo $i (°C): ")
            val temp = readLine()?.toDoubleOrNull() ?: 0.0
            temperaturasModulos.add(temp)

            when {
                temp < 5 -> println("⚠️ Alerta: temperatura muito baixa!")
                temp in 5.0..35.0 -> println("Temperatura estável.")
                temp > 35 -> println("⚠️ Alerta: superaquecimento detectado!")
            }
        }

        val mediaTemp = if (temperaturasModulos.isNotEmpty()) temperaturasModulos.average() else 0.0
        println("Média de temperatura dos módulos: %.2f°C".format(mediaTemp))

        // Verificação de trajes espaciais
        print("\nQuantidade de trajes espaciais para verificar: ")
        val qtdTrajes = readLine()?.toIntOrNull() ?: 0
        var trajesAprovados = 0
        var trajesReprovados = 0

        for (i in 1..qtdTrajes) {
            println("Traje $i:")
            print(" - Pressão (psi): ")
            val pressao = readLine()?.toDoubleOrNull() ?: 0.0
            print(" - Oxigênio (%): ")
            val oxigenio = readLine()?.toDoubleOrNull() ?: 0.0
            print(" - Temperatura interna (°C): ")
            val tempInterna = readLine()?.toDoubleOrNull() ?: 0.0

            val aprovado = pressao in 4.0..6.0 &&
                    oxigenio in 19.0..23.0 &&
                    tempInterna in 18.0..25.0

            if (aprovado) {
                println("Traje aprovado")
                trajesAprovados++
            } else {
                println("Traje reprovado")
                trajesReprovados++
            }
        }

        println("Total de trajes aprovados: $trajesAprovados")
        println("Total de trajes reprovados: $trajesReprovados")

        // Armazenamento da missão
        distancias.add(distancia)
        missoes.add(comandante)

        print("\nDeseja cadastrar outra missão? (sim/não): ")
        continuar = readLine()?.lowercase() ?: "não"
        println()

    } while (continuar == "sim")

    // Relatório geral final
    if (distancias.isNotEmpty()) {
        val media = distancias.average()
        val maior = distancias.maxOrNull() ?: 0.0
        val menor = distancias.minOrNull() ?: 0.0
        val entre50e100 = distancias.count { it in 50.0..100.0 }
        val falhas = distancias.count { it == 0.0 }

        println("===== RELATÓRIO FINAL DAS MISSÕES =====")
        println("Total de missões cadastradas: ${missoes.size}")
        println("Média das distâncias: %.2f milhões de km".format(media))
        println("Maior distância registrada: $maior milhões de km")
        println("Menor distância registrada: $menor milhões de km")
        println("Missões entre 50 e 100 milhões de km: $entre50e100")
        println("Missões com distância 0 (falhas): $falhas")
    } else {
        println("Nenhuma missão foi registrada.")
    }
}
