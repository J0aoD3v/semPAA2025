
# Vamos criar exemplos de código para demonstrar análise amortizada
# 1. Contador Binário - Incremento

def increment_binary_counter(A, k):
    """
    Incrementa um contador binário de k bits
    A: array representando o contador (A[0] é o bit menos significativo)
    k: número de bits
    Retorna: número de bits alterados (custo)
    """
    i = 0
    flips = 0
    while i < k and A[i] == 1:
        A[i] = 0
        flips += 1
        i += 1
    if i < k:
        A[i] = 1
        flips += 1
    return flips

# Simulação de n incrementos em um contador de k bits
def simulate_binary_counter(k, n):
    A = [0] * k  # Contador inicializado com zeros
    total_flips = 0
    operations = []
    
    for i in range(n):
        flips = increment_binary_counter(A, k)
        total_flips += flips
        operations.append({
            'operation': i + 1,
            'flips': flips,
            'counter_value': int(''.join(map(str, A[::-1])), 2) if any(A) else 0
        })
    
    return operations, total_flips

# Exemplo: 16 incrementos em um contador de 5 bits
k = 5
n = 16
operations, total = simulate_binary_counter(k, n)

print("=" * 60)
print("EXEMPLO 1: CONTADOR BINÁRIO")
print("=" * 60)
print(f"Número de bits (k): {k}")
print(f"Número de incrementos (n): {n}")
print(f"\nTotal de bits alterados: {total}")
print(f"Custo amortizado por operação: {total/n:.2f}")
print(f"Análise teórica: O(1) por operação")
print("\nPrimeiras 10 operações:")
print("-" * 60)
print(f"{'Op':<5} {'Bits Alterados':<15} {'Valor':<10}")
print("-" * 60)
for op in operations[:10]:
    print(f"{op['operation']:<5} {op['flips']:<15} {op['counter_value']:<10}")

print("\n" + "=" * 60)
