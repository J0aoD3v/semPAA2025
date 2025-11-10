/*
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
    printf("\n");
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

    printf("Análise Amortizada: Contador Binário\n");
    printf("=====================================\n\n");
    printf("Número de bits (k): %d\n", k);
    printf("Número de incrementos (n): %d\n\n", n);

    int total_flips = 0;

    printf("Op\tBits Alterados\tValor\n");
    printf("-----------------------------------\n");

    for (int i = 1; i <= n; i++) {
        int flips = increment(counter);
        total_flips += flips;

        // Calcula valor decimal
        int valor = 0;
        for (int j = 0; j < k; j++) {
            valor += counter->bits[j] * (1 << j);
        }

        printf("%d\t%d\t\t%d\n", i, flips, valor);
    }

    printf("\n=====================================\n");
    printf("Custo total: %d\n", total_flips);
    printf("Custo amortizado: %.2f\n", (float)total_flips / n);
    printf("Análise teórica: O(1) por operação\n");
    printf("=====================================\n");

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
