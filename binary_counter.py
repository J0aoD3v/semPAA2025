"""
Implementação de um Contador Binário para demonstrar Análise Amortizada.

Este exemplo mostra como incrementos têm custo amortizado O(1),
mesmo que algumas operações individuais sejam O(k) onde k é o número de bits.
"""

class BinaryCounter:
    """
    Contador binário de k bits.
    
    Análise Amortizada:
    - Pior caso de incremento: O(k) quando todos os bits são 1
    - Custo amortizado de incremento: O(1)
    """
    
    def __init__(self, k=8):
        """
        Inicializa contador com k bits.
        
        Args:
            k: Número de bits do contador
        """
        self.k = k
        self.bits = [0] * k
    
    def increment(self):
        """
        Incrementa o contador em 1.
        
        Returns:
            Número de bits modificados (para análise)
        """
        i = 0
        bit_flips = 0
        
        # Propaga o carry
        while i < self.k and self.bits[i] == 1:
            self.bits[i] = 0
            bit_flips += 1
            i += 1
        
        # Seta o próximo bit para 1
        if i < self.k:
            self.bits[i] = 1
            bit_flips += 1
        
        return bit_flips
    
    def value(self):
        """Retorna o valor decimal do contador."""
        result = 0
        for i in range(self.k):
            result += self.bits[i] * (2 ** i)
        return result
    
    def reset(self):
        """Reseta o contador para 0."""
        self.bits = [0] * self.k
    
    def __str__(self):
        """Representação em string do contador (bits mais significativos à esquerda)."""
        return ''.join(map(str, reversed(self.bits)))


def demonstrate_amortized_analysis():
    """
    Demonstra a análise amortizada do contador binário.
    """
    print("=" * 80)
    print("DEMONSTRAÇÃO: Análise Amortizada de Contador Binário")
    print("=" * 80)
    print()
    
    counter = BinaryCounter(8)
    total_flips = 0
    n_increments = 32
    
    print(f"{'Incr':<6} {'Valor':<7} {'Binário':<12} {'Flips':<7} {'Total':<7} {'Média':<8}")
    print("-" * 80)
    
    for i in range(1, n_increments + 1):
        flips = counter.increment()
        total_flips += flips
        avg = total_flips / i
        
        print(f"{i:<6} {counter.value():<7} {str(counter):<12} {flips:<7} {total_flips:<7} {avg:<8.2f}")
    
    print()
    print("=" * 80)
    print("ANÁLISE DOS RESULTADOS")
    print("=" * 80)
    print()
    
    # Análise de frequência de flips
    counter2 = BinaryCounter(8)
    bit_flip_counts = [0] * 8
    
    for _ in range(256):  # Completa todos os valores de 8 bits
        i = 0
        while i < 8 and counter2.bits[i] == 1:
            bit_flip_counts[i] += 1  # Flip de 1 para 0
            counter2.bits[i] = 0
            i += 1
        
        if i < 8:
            bit_flip_counts[i] += 1  # Flip de 0 para 1
            counter2.bits[i] = 1
    
    print("Frequência de flips por bit (em 256 incrementos):")
    print(f"{'Bit':<8} {'Flips':<10} {'Frequência':<12}")
    print("-" * 40)
    
    for i in range(8):
        freq = bit_flip_counts[i] / 256
        expected_freq = 1 / (2 ** i)
        print(f"b{i:<7} {bit_flip_counts[i]:<10} {freq:<12.4f} (esperado: {expected_freq:.4f})")
    
    total_flips_256 = sum(bit_flip_counts)
    avg_flips = total_flips_256 / 256
    
    print()
    print(f"Total de flips em 256 incrementos: {total_flips_256}")
    print(f"Média de flips por incremento: {avg_flips:.2f}")
    print()
    print("CONCLUSÃO: A soma das frequências converge para 2:")
    print(f"Σ(1/2^i) para i=0 a ∞ = 2")
    print(f"Portanto, o custo amortizado é O(1) = ~2 flips por incremento.")
    print()


def demonstrate_three_methods():
    """
    Demonstra os três métodos de análise amortizada no contador binário.
    """
    print("=" * 80)
    print("OS TRÊS MÉTODOS DE ANÁLISE AMORTIZADA - Contador Binário")
    print("=" * 80)
    print()
    
    print("1. MÉTODO AGREGADO")
    print("-" * 80)
    print("Para n incrementos:")
    print("  - Bit b0 muda n vezes")
    print("  - Bit b1 muda n/2 vezes")
    print("  - Bit b2 muda n/4 vezes")
    print("  - Bit bi muda n/2^i vezes")
    print()
    print("Custo total T(n) = Σ(n/2^i) < n × Σ(1/2^i) = n × 2 = 2n")
    print("Custo amortizado = T(n)/n = 2n/n = 2 = O(1)")
    print()
    
    print("2. MÉTODO CONTABILISTA")
    print("-" * 80)
    print("Custo amortizado por incremento: 2 unidades")
    print("  - 1 unidade paga o flip de 0→1")
    print("  - 1 unidade fica como crédito no bit que virou 1")
    print()
    print("Quando um bit muda de 1→0:")
    print("  - O custo é pago pelo crédito armazenado nesse bit")
    print()
    print("Invariante: Todo bit '1' tem 1 unidade de crédito")
    print("Crédito nunca fica negativo → Custo amortizado = O(1)")
    print()
    
    print("3. MÉTODO DO POTENCIAL")
    print("-" * 80)
    print("Função potencial: Φ = número de bits '1' no contador")
    print()
    print("Para incremento que reseta j bits:")
    print("  - Custo real ti = j + 1 (j flips de 1→0, 1 flip de 0→1)")
    print("  - ΔΦ = -j + 1 (perdemos j bits '1', ganhamos 1 bit '1')")
    print("  - Custo amortizado = ti + ΔΦ = (j+1) + (-j+1) = 2")
    print()
    print("Custo amortizado constante = O(1)")
    print()


if __name__ == "__main__":
    demonstrate_amortized_analysis()
    print("\n\n")
    demonstrate_three_methods()
