# semPAA2025
Análise Amortizada

## Definição

**Análise amortizada** é um método para analisar o custo médio de uma sequência de operações, em vez de analisar o pior caso de uma única operação isolada. Este tipo de análise é particularmente útil quando operações esporadicamente caras são compensadas por muitas operações baratas, resultando em um custo total baixo para toda a sequência.

A ideia central é distribuir o custo das operações caras ao longo de toda a sequência, mostrando que o custo médio por operação é menor do que o pior caso individual.

## Os Três Principais Métodos

### 1. Método Agregado (Aggregate Method)

No método agregado, mostramos que para todas as sequências de *n* operações, o custo total é *T(n)*. Portanto, o custo amortizado por operação é *T(n)/n*.

**Vantagens:**
- Simples e direto
- Bom para análise global

**Desvantagens:**
- Não fornece custos individuais por operação
- Menos detalhado que outros métodos

### 2. Método Contabilista ou Bancário (Accounting Method)

No método contabilista, atribuímos custos amortizados diferentes para diferentes operações. Algumas operações são cobradas mais do que seu custo real, e o excesso é armazenado como "crédito" para pagar por operações futuras que custam mais do que seu custo amortizado.

**Princípio fundamental:**
- Custo amortizado ≥ Custo real (para garantir crédito não negativo)
- O crédito acumulado nunca pode ser negativo

**Vantagens:**
- Intuitivo (analogia com banco)
- Custos diferentes por operação

**Desvantagens:**
- Requer rastreamento cuidadoso dos créditos

### 3. Método do Potencial (Potential Method)

O método do potencial usa uma função potencial Φ que mapeia cada estado da estrutura de dados para um número real. O custo amortizado de uma operação é o custo real mais a mudança no potencial.

**Fórmula:**
```
Custo amortizado = Custo real + Φ(estado após) - Φ(estado antes)
```

**Propriedade importante:**
- Φ(estado inicial) = 0
- Φ(qualquer estado) ≥ 0

**Vantagens:**
- Matemáticamente elegante
- Não requer rastreamento explícito de créditos

**Desvantagens:**
- Pode ser difícil encontrar a função potencial correta

## Exemplos Práticos

### Exemplo 1: Operações de Append em um Vetor Dinâmico

Um vetor dinâmico (como `ArrayList` em Java ou `list` em Python) dobra seu tamanho quando fica cheio.

#### Cenário:
- Começamos com um vetor de tamanho 1
- Quando o vetor fica cheio, criamos um novo vetor com o dobro do tamanho
- Copiamos todos os elementos para o novo vetor
- Adicionamos o novo elemento

#### Análise usando Método Agregado:

Para *n* operações de append:
- A maioria das operações tem custo O(1) (apenas adicionar elemento)
- Operações de redimensionamento ocorrem em potências de 2: 1, 2, 4, 8, 16, ..., n
- Custo total de cópias: 1 + 2 + 4 + 8 + ... + n ≤ 2n

**Custo total:** n operações simples + 2n cópias = 3n = O(n)

**Custo amortizado:** O(n)/n = **O(1) por operação**

#### Análise usando Método Contabilista:

- **Custo amortizado por append:** 3 unidades
- **Custo real de append sem redimensionamento:** 1 unidade
- **Crédito armazenado:** 2 unidades por elemento

Quando redimensionamos:
- Temos que copiar k elementos (onde k é o tamanho atual)
- Cada um dos k elementos tem 2 unidades de crédito armazenado
- Crédito total: 2k unidades (suficiente para pagar k cópias + k novos slots)

**Conclusão:** O crédito nunca fica negativo, logo o custo amortizado é O(1).

#### Análise usando Método do Potencial:

**Função potencial:** Φ(vetor) = 2 × (número de elementos) - (capacidade)

- Após inserção sem redimensionamento:
  - Custo real: 1
  - ΔΦ = 2 × 1 = 2
  - Custo amortizado = 1 + 2 = 3

- Após inserção com redimensionamento (de k para 2k):
  - Custo real: k + 1 (copiar k elementos + inserir 1)
  - Φ(antes) = 2k - k = k
  - Φ(depois) = 2(k+1) - 2k = 2
  - ΔΦ = 2 - k
  - Custo amortizado = (k + 1) + (2 - k) = 3

**Conclusão:** Custo amortizado é O(1) em ambos os casos.

### Exemplo 2: Incremento de um Contador Binário

Considere um contador binário de *k* bits, inicialmente zero, e queremos fazer *n* incrementos.

#### Cenário:
- Contador: array de bits [b₀, b₁, b₂, ..., b_{k-1}]
- Incremento: adiciona 1 ao contador

#### Análise de Pior Caso vs. Amortizada:

**Pior caso de uma operação:** O(k) - quando todos os bits são 1 e precisam virar 0, propagando o carry.

#### Análise usando Método Agregado:

Observação: O bit b₀ (menos significativo) muda a cada incremento.
- b₀ muda: n vezes
- b₁ muda: ⌊n/2⌋ vezes
- b₂ muda: ⌊n/4⌋ vezes
- b₃ muda: ⌊n/8⌋ vezes
- ...
- bᵢ muda: ⌊n/2ⁱ⌋ vezes

**Custo total:**
```
T(n) = Σ(i=0 to k-1) ⌊n/2ⁱ⌋ < n × Σ(i=0 to ∞) 1/2ⁱ = n × 2 = 2n
```

**Custo amortizado:** 2n/n = **O(1) por incremento**

#### Análise usando Método Contabilista:

- **Custo amortizado:** 2 unidades por incremento
- **Custo real de mudar um bit de 0 para 1:** 1 unidade (pago pelo custo amortizado)
- **Custo real de mudar um bit de 1 para 0:** 1 unidade (pago pelo crédito armazenado)

**Invariante:** Todo bit 1 no contador tem 1 unidade de crédito.

Quando incrementamos:
- Mudamos alguns bits de 1 para 0 (pagos pelo crédito armazenado)
- Mudamos um bit de 0 para 1 (pago por 1 unidade do custo amortizado)
- A segunda unidade do custo amortizado fica como crédito no novo bit 1

**Conclusão:** Custo amortizado é O(1).

#### Análise usando Método do Potencial:

**Função potencial:** Φ(contador) = número de bits 1 no contador

- **Custo real de incremento:** tᵢ = número de bits mudados (1 bit de 0→1, mais alguns bits de 1→0)
- Se resetamos j bits, então: tᵢ = j + 1
- **ΔΦ:** -j + 1 = -(j-1) (perdemos j bits 1 e ganhamos 1 bit 1)
- **Custo amortizado:** tᵢ + ΔΦ = (j + 1) + (-j + 1) = 2

**Conclusão:** Custo amortizado é O(1).

## Implementação em Python

### Vetor Dinâmico

```python
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity
    
    def append(self, element):
        # Se está cheio, redimensiona
        if self.size == self.capacity:
            self._resize()
        
        # Adiciona o elemento
        self.array[self.size] = element
        self.size += 1
    
    def _resize(self):
        # Dobra a capacidade
        self.capacity *= 2
        new_array = [None] * self.capacity
        
        # Copia elementos (operação cara!)
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array

# Demonstração
arr = DynamicArray()
for i in range(10):
    arr.append(i)
    print(f"Após append {i}: size={arr.size}, capacity={arr.capacity}")
```

### Contador Binário

```python
class BinaryCounter:
    def __init__(self, k):
        self.k = k  # número de bits
        self.bits = [0] * k
    
    def increment(self):
        i = 0
        operations = 0  # conta operações de flip
        
        # Propaga o carry
        while i < self.k and self.bits[i] == 1:
            self.bits[i] = 0
            operations += 1
            i += 1
        
        # Seta o próximo bit para 1
        if i < self.k:
            self.bits[i] = 1
            operations += 1
        
        return operations
    
    def value(self):
        return int(''.join(map(str, reversed(self.bits))), 2)
    
    def __str__(self):
        return ''.join(map(str, reversed(self.bits)))

# Demonstração
counter = BinaryCounter(8)
total_ops = 0
for i in range(1, 17):
    ops = counter.increment()
    total_ops += ops
    print(f"Incremento {i}: {counter} (valor={counter.value()}, ops={ops}, média={total_ops/i:.2f})")
```

## Conclusão

A análise amortizada demonstra que **operações esporadicamente caras podem ter um custo médio muito baixo** quando distribuídas ao longo de uma sequência de operações. Os três métodos (agregado, contabilista e do potencial) oferecem diferentes perspectivas para provar o mesmo resultado:

- **Método Agregado:** Análise global e direta
- **Método Contabilista:** Intuitivo com analogia bancária
- **Método do Potencial:** Matematicamente elegante e sistemático

Nos exemplos práticos:
- **Vetor Dinâmico:** Apesar de redimensionamentos custarem O(n), o custo amortizado de append é O(1)
- **Contador Binário:** Apesar de alguns incrementos custarem O(k), o custo amortizado é O(1)

Esses resultados são fundamentais para entender a eficiência de muitas estruturas de dados modernas, como tabelas hash dinâmicas, filas de prioridade, e estruturas de dados persistentes.
