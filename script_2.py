
# 3. Análise comparativa dos custos

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Dados do contador binário
k = 8
n_counter = 100
ops_counter, total_counter = simulate_binary_counter(k, n_counter)

# Dados do vetor dinâmico
n_array = 100
ops_array, total_array = simulate_dynamic_array(n_array)

# Criar gráfico comparativo
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Gráfico 1: Custo por operação - Contador Binário
ax1 = axes[0, 0]
operations_num = [op['operation'] for op in ops_counter]
flips = [op['flips'] for op in ops_counter]
ax1.bar(operations_num, flips, color='steelblue', alpha=0.7)
ax1.axhline(y=total_counter/n_counter, color='red', linestyle='--', 
            label=f'Custo amortizado = {total_counter/n_counter:.2f}')
ax1.set_xlabel('Operação', fontsize=10)
ax1.set_ylabel('Bits Alterados', fontsize=10)
ax1.set_title('Contador Binário: Custo por Operação', fontsize=12, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico 2: Custo acumulado - Contador Binário
ax2 = axes[0, 1]
cumulative_counter = np.cumsum([op['flips'] for op in ops_counter])
worst_case = [k * i for i in range(1, n_counter + 1)]
ax2.plot(operations_num, cumulative_counter, 'b-', linewidth=2, label='Custo Real')
ax2.plot(operations_num, worst_case, 'r--', linewidth=2, label='Pior Caso (O(nk))')
ax2.set_xlabel('Número de Operações', fontsize=10)
ax2.set_ylabel('Custo Acumulado', fontsize=10)
ax2.set_title('Contador Binário: Custo Acumulado', fontsize=12, fontweight='bold')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Gráfico 3: Custo por operação - Vetor Dinâmico
ax3 = axes[1, 0]
operations_array = [op['operation'] for op in ops_array]
costs = [op['cost'] for op in ops_array]
colors = ['red' if op['is_resize'] else 'steelblue' for op in ops_array]
ax3.bar(operations_array, costs, color=colors, alpha=0.7)
ax3.axhline(y=total_array/n_array, color='green', linestyle='--', 
            label=f'Custo amortizado = {total_array/n_array:.2f}')
ax3.set_xlabel('Operação', fontsize=10)
ax3.set_ylabel('Custo', fontsize=10)
ax3.set_title('Vetor Dinâmico: Custo por Operação\n(Vermelho = Resize)', 
              fontsize=12, fontweight='bold')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Gráfico 4: Custo acumulado - Vetor Dinâmico
ax4 = axes[1, 1]
cumulative_array = np.cumsum([op['cost'] for op in ops_array])
worst_case_array = [i**2 for i in range(1, n_array + 1)]  # Se realocasse a cada inserção
ax4.plot(operations_array, cumulative_array, 'b-', linewidth=2, label='Custo Real (Doubling)')
ax4.plot(operations_array, operations_array, 'g--', linewidth=2, 
         label='Linear (Amortizado)')
ax4.set_xlabel('Número de Operações', fontsize=10)
ax4.set_ylabel('Custo Acumulado', fontsize=10)
ax4.set_title('Vetor Dinâmico: Custo Acumulado', fontsize=12, fontweight='bold')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('analise_amortizada_exemplos.png', dpi=150, bbox_inches='tight')
print("Gráfico salvo como 'analise_amortizada_exemplos.png'")
print("\nOs gráficos mostram:")
print("1. Contador Binário: A maioria das operações tem custo baixo")
print("2. Vetor Dinâmico: Operações caras (resize) são raras e esparsas")
print("3. Em ambos: o custo amortizado é muito menor que o pior caso individual")
