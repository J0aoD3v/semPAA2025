# Vetor Dinâmico - Análise Amortizada
# Exemplo para seminário de PAA

class VetorDinamico:
    """
    Implementação de um vetor dinâmico com redimensionamento
    usando a técnica de doubling (duplicação de capacidade)
    """

    def __init__(self):
        self.capacidade = 1
        self.tamanho = 0
        self.array = [None] * self.capacidade

    def append(self, valor):
        """
        Adiciona um elemento ao final do vetor
        Retorna o custo da operação (número de elementos copiados + 1)
        """
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
        """Duplica a capacidade do array"""
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
    """Demonstra o funcionamento do vetor dinâmico"""
    vetor = VetorDinamico()

    print("Análise Amortizada: Vetor Dinâmico")
    print("=" * 60)
    print(f"Número de inserções: {n}\n")

    print(f"{'Op':<5} {'Custo':<8} {'Tamanho':<10} {'Capacidade':<12} {'Resize?'}")
    print("-" * 60)

    custo_total = 0

    for i in range(1, n + 1):
        custo = vetor.append(i)
        custo_total += custo
        resize = "SIM" if custo > 1 else "NÃO"

        print(f"{i:<5} {custo:<8} {vetor.tamanho:<10} {vetor.capacidade:<12} {resize}")

    print("\n" + "=" * 60)
    print(f"Custo total: {custo_total}")
    print(f"Custo amortizado: {custo_total/n:.2f}")
    print(f"Análise teórica: O(1) por operação")
    print("=" * 60)

    return vetor


# Exemplo de uso
if __name__ == "__main__":
    n = 20
    vetor = demonstrar_vetor_dinamico(n)

    print(f"\nVetor final: {vetor}")
    print(f"Info: {vetor.info()}")

"""
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
"""
