// Vetor Dinâmico - Conversão de vetor_dinamico.py para C
// Exemplo para seminário de PAA (Análise Amortizada)

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int capacidade;
    int tamanho;
    int *array;
} VetorDinamico;

VetorDinamico *vetor_criar(void) {
    VetorDinamico *v = malloc(sizeof(VetorDinamico));
    if (!v) {
        fprintf(stderr, "Erro: malloc falhou\n");
        exit(EXIT_FAILURE);
    }
    v->capacidade = 1;
    v->tamanho = 0;
    v->array = malloc(v->capacidade * sizeof(int));
    if (!v->array) {
        fprintf(stderr, "Erro: malloc falhou\n");
        free(v);
        exit(EXIT_FAILURE);
    }
    return v;
}

// Redimensiona (duplica) a capacidade. Retorna o número de elementos copiados.
static int vetor_redimensionar(VetorDinamico *v) {
    int antigos = v->tamanho;
    int nova_cap = v->capacidade * 2;
    int *novo = malloc(nova_cap * sizeof(int));
    if (!novo) {
        fprintf(stderr, "Erro: malloc falhou ao redimensionar\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < v->tamanho; ++i) {
        novo[i] = v->array[i];
    }
    free(v->array);
    v->array = novo;
    v->capacidade = nova_cap;
    return antigos; // número de elementos copiados
}

// Adiciona um valor ao final. Retorna o custo (1 pela inserção + cópias se redimensionar)
int vetor_append(VetorDinamico *v, int valor) {
    int custo = 1; // custo de inserir o elemento
    if (v->tamanho == v->capacidade) {
        int copiados = vetor_redimensionar(v);
        custo += copiados; // custo de copiar elementos durante resize
    }
    v->array[v->tamanho] = valor;
    v->tamanho += 1;
    return custo;
}

void vetor_imprimir(VetorDinamico *v) {
    printf("[");
    for (int i = 0; i < v->tamanho; ++i) {
        printf("%d", v->array[i]);
        if (i + 1 < v->tamanho) printf(", ");
    }
    printf("]\n");
}

void vetor_info(VetorDinamico *v) {
    printf("Info: Tamanho: %d, Capacidade: %d\n", v->tamanho, v->capacidade);
}

void demonstrar_vetor_dinamico(int n) {
    VetorDinamico *vetor = vetor_criar();

    printf("An\u00e1lise Amortizada: Vetor Din\u00e2mico\n");
    printf("============================================================\n");
    printf("N\u00famero de inser\u00e7\u00f5es: %d\n\n", n);

    printf("% -5s % -8s % -10s % -12s %s\n", "Op", "Custo", "Tamanho", "Capacidade", "Resize?");
    printf("------------------------------------------------------------\n");

    int custo_total = 0;
    for (int i = 1; i <= n; ++i) {
        int custo = vetor_append(vetor, i);
        custo_total += custo;
        const char *resize = (custo > 1) ? "SIM" : "N\xc3\x83O"; // NÃO
        printf("% -5d % -8d % -10d % -12d %s\n", i, custo, vetor->tamanho, vetor->capacidade, resize);
    }

    printf("\n============================================================\n");
    printf("Custo total: %d\n", custo_total);
    printf("Custo amortizado: %.2f\n", custo_total / (double)n);
    printf("An\u00e1lise te\u00f3rica: O(1) por opera\u00e7\u00e3o\n");
    printf("============================================================\n");

    printf("\nVetor final: ");
    vetor_imprimir(vetor);
    vetor_info(vetor);

    free(vetor->array);
    free(vetor);
}

int main(void) {
    int n = 20;
    demonstrar_vetor_dinamico(n);
    return 0;
}

/*
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
*/
