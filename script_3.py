
# Vamos criar um resumo de complexidades para apresentação

summary = """
RESUMO: ANÁLISE AMORTIZADA - COMPLEXIDADES

1. CONTADOR BINÁRIO (INCREMENT)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Operação: Incrementar contador de k bits
   
   Pior Caso (uma operação):
   - Temporal: O(k) - quando todos os bits são 1
   - Espacial: O(k) - armazenamento do contador
   
   Melhor Caso (uma operação):
   - Temporal: O(1) - quando apenas o bit 0 muda
   - Espacial: O(k)
   
   Análise Amortizada (sequência de n operações):
   - Custo total: O(n) 
   - Custo amortizado por operação: O(1)
   - Método: Agregado, Contabilista ou Potencial

2. VETOR DINÂMICO (APPEND com DOUBLING)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Operação: Inserir elemento no final do vetor
   
   Pior Caso (uma operação):
   - Temporal: O(n) - quando precisa redimensionar e copiar
   - Espacial: O(n) - novo array é alocado
   
   Melhor Caso (uma operação):
   - Temporal: O(1) - quando há espaço disponível
   - Espacial: O(1) - não aloca memória adicional
   
   Análise Amortizada (sequência de n operações):
   - Custo total: O(n)
   - Custo amortizado por operação: O(1)
   - Método: Agregado, Contabilista ou Potencial
   
   Memória total no pior caso: O(n) - até 2n espaços

3. MÉTODOS DE ANÁLISE AMORTIZADA
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   
   a) MÉTODO AGREGADO:
      - Calcula custo total T(n) de n operações
      - Custo amortizado = T(n) / n
      - Mais simples e direto
   
   b) MÉTODO CONTABILISTA (BANCÁRIO):
      - Atribui créditos às operações
      - Operações baratas "poupam" para operações caras
      - Saldo nunca pode ser negativo
   
   c) MÉTODO DO POTENCIAL:
      - Define função potencial Φ(Di)
      - Custo amortizado = Custo real + ΔΦ
      - Φ(D0) = 0 e Φ(Di) ≥ 0 para todo i
      - Mais flexível e poderoso

OBSERVAÇÕES IMPORTANTES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Análise amortizada ≠ Análise de caso médio
✓ Análise amortizada é uma análise de pior caso sobre sequências
✓ Não usa probabilidade ou distribuições de entrada
✓ Garante desempenho médio mesmo no pior cenário possível
"""

print(summary)

# Criar arquivo com o resumo
with open('complexidades_resumo.txt', 'w', encoding='utf-8') as f:
    f.write(summary)

print("\n" + "="*60)
print("Arquivo 'complexidades_resumo.txt' criado com sucesso!")
print("="*60)
