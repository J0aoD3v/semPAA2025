
# 2. Vetor Dinâmico com Append (Doubling)

class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity
        
    def append(self, value):
        """
        Adiciona um elemento ao final do vetor
        Retorna o custo da operação (número de elementos copiados + 1 para inserção)
        """
        cost = 1  # custo de inserir o elemento
        
        # Se o array está cheio, duplica o tamanho
        if self.size == self.capacity:
            old_capacity = self.capacity
            self.capacity *= 2
            new_array = [None] * self.capacity
            
            # Copia todos os elementos (custo = tamanho atual)
            for i in range(self.size):
                new_array[i] = self.array[i]
            
            cost += self.size  # custo de copiar elementos
            self.array = new_array
        
        # Insere o novo elemento
        self.array[self.size] = value
        self.size += 1
        
        return cost

# Simulação de inserções
def simulate_dynamic_array(n):
    arr = DynamicArray()
    operations = []
    total_cost = 0
    
    for i in range(1, n + 1):
        cost = arr.append(i)
        total_cost += cost
        operations.append({
            'operation': i,
            'cost': cost,
            'size': arr.size,
            'capacity': arr.capacity,
            'is_resize': cost > 1
        })
    
    return operations, total_cost

# Exemplo: 20 inserções
n = 20
operations, total = simulate_dynamic_array(n)

print("EXEMPLO 2: VETOR DINÂMICO (DOUBLING)")
print("=" * 60)
print(f"Número de inserções (n): {n}")
print(f"\nCusto total: {total}")
print(f"Custo amortizado por operação: {total/n:.2f}")
print(f"Análise teórica: O(1) por operação")
print("\nOperações realizadas:")
print("-" * 60)
print(f"{'Op':<5} {'Custo':<8} {'Size':<8} {'Capacity':<10} {'Resize?':<10}")
print("-" * 60)
for op in operations:
    resize = "SIM" if op['is_resize'] else "NÃO"
    print(f"{op['operation']:<5} {op['cost']:<8} {op['size']:<8} {op['capacity']:<10} {resize:<10}")

print("\n" + "=" * 60)
