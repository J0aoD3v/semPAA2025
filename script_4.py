
# Vamos criar códigos exemplo em C e Python para a apresentação

# Código C para contador binário
codigo_c_contador = """/*
 * Contador Binário - Análise Amortizada
 * Exemplo para seminário de PAA
 */

#include <stdio.h>
#include <stdlib.h>

// Estrutura do contador binário
typedef struct {
    int *bits;     // Array de bits
    int k;         // Número de bits
} BinaryCounter;

// Inicializa contador com k bits (todos zerados)
BinaryCounter* criar_contador(int k) {
    BinaryCounter *counter = (BinaryCounter*)malloc(sizeof(BinaryCounter));
    counter->bits = (int*)calloc(k, sizeof(int));
    counter->k = k;
    return counter;
}

// Incrementa o contador binário
// Retorna: número de bits alterados (custo da operação)
int increment(BinaryCounter *counter) {
    int i = 0;
    int flips = 0;
    
    // Propaga o carry enquanto encontrar bits 1
    while (i < counter->k && counter->bits[i] == 1) {
        counter->bits[i] = 0;
        flips++;
        i++;
    }
    
    // Se não ultrapassou o limite, coloca 1
    if (i < counter->k) {
        counter->bits[i] = 1;
        flips++;
    }
    
    return flips;
}

// Imprime o contador
void imprimir_contador(BinaryCounter *counter) {
    printf("Contador: ");
    for (int i = counter->k - 1; i >= 0; i--) {
        printf("%d", counter->bits[i]);
    }
    printf("\\n");
}

// Libera memória
void destruir_contador(BinaryCounter *counter) {
    free(counter->bits);
    free(counter);
}

int main() {
    int k = 5;  // 5 bits
    int n = 16; // 16 incrementos
    
    BinaryCounter *counter = criar_contador(k);
    
    printf("Análise Amortizada: Contador Binário\\n");
    printf("=====================================\\n\\n");
    printf("Número de bits (k): %d\\n", k);
    printf("Número de incrementos (n): %d\\n\\n", n);
    
    int total_flips = 0;
    
    printf("Op\\tBits Alterados\\tValor\\n");
    printf("-----------------------------------\\n");
    
    for (int i = 1; i <= n; i++) {
        int flips = increment(counter);
        total_flips += flips;
        
        // Calcula valor decimal
        int valor = 0;
        for (int j = 0; j < k; j++) {
            valor += counter->bits[j] * (1 << j);
        }
        
        printf("%d\\t%d\\t\\t%d\\n", i, flips, valor);
    }
    
    printf("\\n=====================================\\n");
    printf("Custo total: %d\\n", total_flips);
    printf("Custo amortizado: %.2f\\n", (float)total_flips / n);
    printf("Análise teórica: O(1) por operação\\n");
    printf("=====================================\\n");
    
    destruir_contador(counter);
    return 0;
}

/*
 * COMPLEXIDADE TEMPORAL:
 * - Pior caso (uma operação): O(k)
 * - Melhor caso (uma operação): O(1)
 * - Amortizada (n operações): O(1) por operação
 * 
 * COMPLEXIDADE ESPACIAL: O(k)
 */
"""

# Código Python para vetor dinâmico
codigo_python_vetor = """# Vetor Dinâmico - Análise Amortizada
# Exemplo para seminário de PAA

class VetorDinamico:
    \"\"\"
    Implementação de um vetor dinâmico com redimensionamento
    usando a técnica de doubling (duplicação de capacidade)
    \"\"\"
    
    def __init__(self):
        self.capacidade = 1
        self.tamanho = 0
        self.array = [None] * self.capacidade
    
    def append(self, valor):
        \"\"\"
        Adiciona um elemento ao final do vetor
        Retorna o custo da operação (número de elementos copiados + 1)
        \"\"\"
        custo = 1  # custo de inserir o elemento
        
        # Se o array está cheio, duplica o tamanho
        if self.tamanho == self.capacidade:
            self._redimensionar()
            custo += self.tamanho - 1  # custo de copiar elementos
        
        # Insere o novo elemento
        self.array[self.tamanho] = valor
        self.tamanho += 1
        
        return custo
    
    def _redimensionar(self):
        \"\"\"Duplica a capacidade do array\"\"\"
        self.capacidade *= 2
        novo_array = [None] * self.capacidade
        
        # Copia todos os elementos
        for i in range(self.tamanho):
            novo_array[i] = self.array[i]
        
        self.array = novo_array
    
    def __str__(self):
        elementos = [str(self.array[i]) for i in range(self.tamanho)]
        return f"[{', '.join(elementos)}]"
    
    def info(self):
        return f"Tamanho: {self.tamanho}, Capacidade: {self.capacidade}"


def demonstrar_vetor_dinamico(n):
    \"\"\"Demonstra o funcionamento do vetor dinâmico\"\"\"
    vetor = VetorDinamico()
    
    print("Análise Amortizada: Vetor Dinâmico")
    print("=" * 60)
    print(f"Número de inserções: {n}\\n")
    
    print(f"{'Op':<5} {'Custo':<8} {'Tamanho':<10} {'Capacidade':<12} {'Resize?'}")
    print("-" * 60)
    
    custo_total = 0
    
    for i in range(1, n + 1):
        custo = vetor.append(i)
        custo_total += custo
        resize = "SIM" if custo > 1 else "NÃO"
        
        print(f"{i:<5} {custo:<8} {vetor.tamanho:<10} {vetor.capacidade:<12} {resize}")
    
    print("\\n" + "=" * 60)
    print(f"Custo total: {custo_total}")
    print(f"Custo amortizado: {custo_total/n:.2f}")
    print(f"Análise teórica: O(1) por operação")
    print("=" * 60)
    
    return vetor


# Exemplo de uso
if __name__ == "__main__":
    n = 20
    vetor = demonstrar_vetor_dinamico(n)
    
    print(f"\\nVetor final: {vetor}")
    print(f"Info: {vetor.info()}")

\"\"\"
COMPLEXIDADE TEMPORAL:
- Pior caso (uma operação): O(n) - quando redimensiona
- Melhor caso (uma operação): O(1) - quando há espaço
- Amortizada (n operações): O(1) por operação

COMPLEXIDADE ESPACIAL:
- Total: O(n)
- Overhead: até 2n espaços no pior caso (fator 2)

MÉTODO DE ANÁLISE:
Pode ser analisado por qualquer um dos três métodos:
1. Método Agregado
2. Método Contabilista (atribuir crédito 3 por inserção)
3. Método do Potencial (Φ = 2n - capacidade)
\"\"\"
"""

# Salvar os códigos
with open('contador_binario.c', 'w', encoding='utf-8') as f:
    f.write(codigo_c_contador)

with open('vetor_dinamico.py', 'w', encoding='utf-8') as f:
    f.write(codigo_python_vetor)

print("=" * 60)
print("CÓDIGOS EXEMPLO CRIADOS COM SUCESSO!")
print("=" * 60)
print("\n1. contador_binario.c")
print("   - Implementação em C do contador binário")
print("   - Demonstra o incremento e conta bits alterados")
print("   - Inclui análise de complexidade\n")

print("2. vetor_dinamico.py")
print("   - Implementação em Python do vetor dinâmico")
print("   - Usa técnica de doubling")
print("   - Mostra custos de cada operação\n")

print("=" * 60)
print("\nPara compilar e executar o código C:")
print("  gcc contador_binario.c -o contador")
print("  ./contador")
print("\nPara executar o código Python:")
print("  python vetor_dinamico.py")
print("=" * 60)
