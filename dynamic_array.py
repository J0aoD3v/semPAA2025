"""
Implementação de um Vetor Dinâmico para demonstrar Análise Amortizada.

Este exemplo mostra como operações de append têm custo amortizado O(1),
mesmo que algumas operações individuais (redimensionamento) sejam O(n).
"""

class DynamicArray:
    """
    Vetor dinâmico que dobra de tamanho quando fica cheio.
    
    Análise Amortizada:
    - Custo real de append sem redimensionamento: O(1)
    - Custo real de append com redimensionamento: O(n)
    - Custo amortizado de append: O(1)
    """
    
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity
        self.resize_count = 0
        self.total_copies = 0
    
    def append(self, element):
        """
        Adiciona um elemento ao final do vetor.
        
        Args:
            element: Elemento a ser adicionado
        
        Returns:
            Número de operações realizadas (para análise)
        """
        operations = 0
        
        # Se está cheio, redimensiona
        if self.size == self.capacity:
            operations += self._resize()
        
        # Adiciona o elemento
        self.array[self.size] = element
        self.size += 1
        operations += 1
        
        return operations
    
    def _resize(self):
        """
        Dobra a capacidade do vetor.
        
        Returns:
            Número de cópias realizadas
        """
        # Dobra a capacidade
        old_capacity = self.capacity
        self.capacity *= 2
        new_array = [None] * self.capacity
        
        # Copia elementos (operação cara!)
        copies = 0
        for i in range(self.size):
            new_array[i] = self.array[i]
            copies += 1
        
        self.array = new_array
        self.resize_count += 1
        self.total_copies += copies
        
        return copies
    
    def get(self, index):
        """Retorna o elemento na posição index."""
        if 0 <= index < self.size:
            return self.array[index]
        raise IndexError("Index fora dos limites")
    
    def __str__(self):
        """Representação em string do vetor."""
        elements = [str(self.array[i]) for i in range(self.size)]
        return f"[{', '.join(elements)}]"
    
    def stats(self):
        """Retorna estatísticas sobre o vetor."""
        return {
            'size': self.size,
            'capacity': self.capacity,
            'resize_count': self.resize_count,
            'total_copies': self.total_copies,
            'avg_operations': (self.size + self.total_copies) / self.size if self.size > 0 else 0
        }


def demonstrate_amortized_analysis():
    """
    Demonstra a análise amortizada do vetor dinâmico.
    """
    print("=" * 70)
    print("DEMONSTRAÇÃO: Análise Amortizada de Vetor Dinâmico")
    print("=" * 70)
    print()
    
    arr = DynamicArray()
    total_operations = 0
    
    print(f"{'i':<5} {'Operação':<15} {'Ops':<5} {'Size':<6} {'Cap':<6} {'Média':<8}")
    print("-" * 70)
    
    for i in range(20):
        ops = arr.append(i)
        total_operations += ops
        avg = total_operations / (i + 1)
        
        op_type = "append+resize" if ops > 2 else "append"
        print(f"{i:<5} {op_type:<15} {ops:<5} {arr.size:<6} {arr.capacity:<6} {avg:<8.2f}")
    
    print()
    print("=" * 70)
    print("RESULTADOS DA ANÁLISE AMORTIZADA")
    print("=" * 70)
    
    stats = arr.stats()
    print(f"Total de elementos inseridos: {stats['size']}")
    print(f"Capacidade final: {stats['capacity']}")
    print(f"Número de redimensionamentos: {stats['resize_count']}")
    print(f"Total de cópias realizadas: {stats['total_copies']}")
    print(f"Total de operações: {total_operations}")
    print(f"Média de operações por append: {stats['avg_operations']:.2f}")
    print()
    print("CONCLUSÃO: Apesar de alguns appends custarem O(n) devido ao")
    print("redimensionamento, o custo amortizado é O(1) = ~3 operações por append.")
    print()


if __name__ == "__main__":
    demonstrate_amortized_analysis()
