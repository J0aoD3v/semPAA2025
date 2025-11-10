# Seminário: Análise Amortizada
**Disciplina:** Projeto e Análise de Algoritmos (PAA)  
**Duração:** 30-45 minutos  
**Data:** Novembro de 2025

---

## 1. Introdução

### O que é Análise Amortizada?

**Análise amortizada** é um método para analisar o custo médio de uma **sequência de operações**, em vez de analisar o pior caso de uma única operação isolada.

**Diferença fundamental:**
- **Análise tradicional de pior caso:** foca em UMA operação mais cara
- **Análise amortizada:** distribui o custo total de TODAS as operações

**Não confundir com:**
- **Análise de caso médio:** que usa probabilidade e assume distribuições de entrada
- **Análise amortizada:** é uma análise de pior caso, mas sobre sequências completas

### Quando Usar?

A análise amortizada é útil quando:
- Operações caras são esporadicamente executadas
- Essas operações caras são precedidas por muitas operações baratas
- O pior caso individual dá uma análise pessimista demais

**Exemplo típico:** estruturas de dados onde operações ocasionalmente requerem reorganização (como vetores dinâmicos, tabelas hash com rehashing, árvores de busca auto-balanceadas).

---

## 2. Os Três Métodos de Análise Amortizada

### 2.1 Método Agregado (Aggregate Method)

**Ideia:** Calcular o custo total T(n) de uma sequência de n operações e dividir por n.

**Fórmula:**
```
Custo amortizado = T(n) / n
```

**Características:**
- Método mais direto e intuitivo
- Todas as operações têm o mesmo custo amortizado
- Útil quando é fácil calcular o custo total

**Vantagens:**
✓ Simples de entender e aplicar  
✓ Não requer estruturas auxiliares

**Desvantagens:**
✗ Nem sempre é fácil calcular T(n) diretamente  
✗ Não distingue custos entre diferentes tipos de operações

---

### 2.2 Método Contabilista ou Bancário (Accounting Method)

**Ideia:** Atribuir um **custo amortizado** (fictício) a cada operação, que pode ser diferente do custo real.

**Conceito de "crédito":**
- Se custo amortizado > custo real → **guarda créditos** para o futuro
- Se custo amortizado < custo real → **usa créditos** guardados anteriormente

**Regra fundamental:**
```
Σ(custo amortizado) ≥ Σ(custo real)
```

O saldo de créditos NUNCA pode ser negativo!

**Características:**
- Operações baratas "poupam" para operações caras
- Cada operação pode ter custo amortizado diferente
- Créditos são associados a objetos específicos na estrutura

**Analogia bancária:**
- Operações baratas: depositam dinheiro no banco
- Operações caras: sacam dinheiro do banco
- Saldo bancário: sempre não-negativo

---

### 2.3 Método do Potencial (Potential Method)

**Ideia:** Definir uma **função potencial Φ** que mapeia cada estado da estrutura de dados para um número real não-negativo.

**Definição formal:**

Seja Di o estado da estrutura após a i-ésima operação:

```
Custo amortizado da operação i = custo real + Φ(Di) - Φ(Di-1)
                                = custo real + ΔΦ
```

**Condições necessárias:**
1. Φ(D₀) = 0 (potencial inicial é zero)
2. Φ(Di) ≥ 0 para todo i (potencial sempre não-negativo)

**Interpretação:**
- Φ(Di) = "energia potencial" armazenada na estrutura
- Se ΔΦ > 0: operação "carrega" a estrutura com potencial
- Se ΔΦ < 0: operação "libera" potencial para pagar seu custo

**Características:**
- Mais flexível que o método contabilista
- Atribui potencial à estrutura inteira, não a objetos individuais
- Escolher Φ adequado é a chave da análise

**Vantagens:**
✓ Mais poderoso e geral  
✓ Frequentemente mais elegante matematicamente  
✓ Útil para análises complexas

**Desvantagens:**
✗ Pode ser difícil encontrar Φ adequado  
✗ Menos intuitivo que método contabilista

---

## 3. Exemplo 1: Contador Binário

### Descrição do Problema

Um contador binário de **k bits** representado como array A[0..k-1], onde:
- A[0] é o bit menos significativo (LSB)
- A[k-1] é o bit mais significativo (MSB)
- Valor representado: x = Σ A[i]·2^i

**Operação:** `INCREMENT` - adiciona 1 ao contador

### Algoritmo

```
INCREMENT(A, k)
1.  i ← 0
2.  while i < k and A[i] = 1
3.      A[i] ← 0
4.      i ← i + 1
5.  if i < k
6.      A[i] ← 1
```

### Análise de Pior Caso (Ingênua)

- **Pior caso de uma operação:** O(k) - quando todos os bits são 1
- **n operações:** O(nk) no pior caso

**Mas isso é muito pessimista!** Nem toda operação pode ser O(k).

---

### Análise com Método Agregado

**Observação chave:** Quantas vezes cada bit muda em n incrementos?

- Bit 0: muda a **cada** incremento → n vezes
- Bit 1: muda a **cada 2** incrementos → n/2 vezes
- Bit 2: muda a **cada 4** incrementos → n/4 vezes
- Bit i: muda a cada 2^i incrementos → n/2^i vezes

**Custo total:**
```
T(n) = Σ(i=0 até k-1) ⌊n/2^i⌋
     < Σ(i=0 até ∞) n/2^i
     = n · Σ(i=0 até ∞) 1/2^i
     = n · 2
     = 2n
```

**Portanto:** T(n) = O(n)

**Custo amortizado por operação:** T(n)/n = O(n)/n = **O(1)**

---

### Análise com Método Contabilista

**Ideia:** Atribuir **2 créditos** para cada operação INCREMENT.

**Uso dos créditos:**
1. **1 crédito** paga a mudança do bit 0→1 (linha 6)
2. **1 crédito** fica "guardado" sobre o bit que mudou para 1

**Quando bit muda de 1→0 (linha 3):**
- Usa o crédito guardado sobre aquele bit
- Não precisa pagar nada extra!

**Invariante:** Cada bit com valor 1 tem 1 crédito guardado

**Análise:**
- Custo amortizado: 2 por operação
- Saldo de créditos: sempre ≥ 0 (número de bits 1)
- Custo amortizado: **O(1)**

---

### Análise com Método do Potencial

**Função potencial:** Φ(D) = número de bits 1 no contador

**Condições:**
- Φ(D₀) = 0 ✓ (contador inicia zerado)
- Φ(Di) ≥ 0 ✓ (sempre não-negativo)

**Análise de uma operação:**

Suponha que a operação muda ti bits (ti bits de 1→0, mais 1 bit de 0→1):
- **Custo real:** ci = ti + 1
- **Mudança de potencial:** ΔΦ = -ti + 1 (perdeu ti bits 1, ganhou 1 bit 1)

**Custo amortizado:**
```
ĉi = ci + ΔΦ
   = (ti + 1) + (-ti + 1)
   = 2
```

**Portanto:** Custo amortizado = **O(1)**

---

### Implementação e Demonstração

```c
// Código em C - contador_binario.c
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
    
    return flips; // retorna custo da operação
}
```

**Resultados de execução (k=5, n=16):**

| Operação | Bits Alterados | Valor | Observação |
|----------|----------------|-------|------------|
| 1 | 1 | 1 | 00001 |
| 2 | 2 | 2 | 00010 |
| 3 | 1 | 3 | 00011 |
| 4 | 3 | 4 | 00100 |
| 8 | 4 | 8 | 01000 |
| 16 | 5 | 16 | 10000 |

- **Custo total:** 31 bits alterados
- **Custo amortizado:** 31/16 ≈ 1.94 ≈ **O(1)** ✓

---

## 4. Exemplo 2: Vetor Dinâmico com Append

### Descrição do Problema

**Vetor dinâmico:** estrutura que automaticamente redimensiona quando fica cheia.

**Técnica de doubling:**
- Inicia com capacidade pequena (ex: 1)
- Quando cheio, duplica a capacidade
- Copia todos os elementos para o novo array

### Operação Append

```python
def append(self, valor):
    if self.tamanho == self.capacidade:
        # Redimensiona: duplica capacidade
        self._redimensionar()
    
    self.array[self.tamanho] = valor
    self.tamanho += 1
```

### Análise de Pior Caso (Ingênua)

- **Pior caso de um append:** O(n) - quando precisa redimensionar
- **n operações:** O(n²) no pior caso

**Novamente, muito pessimista!**

---

### Análise com Método Agregado

**Quando ocorrem redimensionamentos?**

Quando tamanho passa de: 1→2, 2→4, 4→8, 8→16, ..., 2^(k-1)→2^k

**Custo de cada redimensionamento:**
- De capacidade 1 para 2: copia 1 elemento
- De capacidade 2 para 4: copia 2 elementos
- De capacidade 4 para 8: copia 4 elementos
- ...
- De capacidade 2^(k-1) para 2^k: copia 2^(k-1) elementos

**Custo total de n inserções:**
```
T(n) = n (inserções) + (1 + 2 + 4 + ... + 2^k) (cópias em redimensionamentos)
     = n + Σ(i=0 até k) 2^i, onde 2^k < n ≤ 2^(k+1)
     = n + (2^(k+1) - 1)
     < n + 2n
     = 3n
```

**Portanto:** T(n) = O(n)

**Custo amortizado por operação:** T(n)/n = **O(1)**

---

### Análise com Método Contabilista

**Ideia:** Atribuir **3 créditos** para cada inserção.

**Uso dos créditos:**
1. **1 crédito** paga a inserção do próprio elemento
2. **1 crédito** guardado sobre o próprio elemento (pagará sua cópia futura)
3. **1 crédito** paga a cópia de um elemento já inserido anteriormente

**Quando redimensiona:**
- Cada elemento já tem 1 crédito guardado
- Usa esses créditos para pagar todas as cópias
- Não precisa pagar nada extra!

**Invariante:** Após n operações, há pelo menos n créditos guardados

**Análise:**
- Custo amortizado: 3 por operação
- Custo amortizado: **O(1)**

---

### Análise com Método do Potencial

**Função potencial:** Φ(D) = 2·tamanho - capacidade

**Verificação:**
- Φ(D₀) = 2·0 - 1 = -1... ❌ (não funciona!)

**Melhor função:** Φ(D) = 2·tamanho - capacidade, se tamanho > 0; 0 caso contrário

Ou simplesmente: **Φ(D) = max(0, 2·tamanho - capacidade)**

**Análise:**

**Caso 1: Inserção sem redimensionamento**
- Custo real: 1
- ΔΦ = 2 (tamanho aumenta 1, capacidade constante)
- Custo amortizado: 1 + 2 = 3

**Caso 2: Inserção com redimensionamento**
- Custo real: tamanho + 1 (copia todos + insere)
- Antes: tamanho = capacidade = n
- Depois: tamanho = n+1, capacidade = 2n
- Φ(antes) = 2n - n = n
- Φ(depois) = 2(n+1) - 2n = 2
- ΔΦ = 2 - n = -(n-2)
- Custo amortizado: (n+1) + (-(n-2)) = 3

**Em ambos os casos:** Custo amortizado = **O(1)**

---

### Implementação e Demonstração

```python
# Código em Python - vetor_dinamico.py
class VetorDinamico:
    def __init__(self):
        self.capacidade = 1
        self.tamanho = 0
        self.array = [None] * self.capacidade
    
    def append(self, valor):
        custo = 1
        
        if self.tamanho == self.capacidade:
            self._redimensionar()
            custo += self.tamanho - 1
        
        self.array[self.tamanho] = valor
        self.tamanho += 1
        return custo
```

**Resultados de execução (n=20):**

| Op | Custo | Tamanho | Capacidade | Resize? |
|----|-------|---------|------------|---------|
| 1 | 1 | 1 | 1 | NÃO |
| 2 | 2 | 2 | 2 | **SIM** |
| 3 | 3 | 3 | 4 | **SIM** |
| 5 | 5 | 5 | 8 | **SIM** |
| 9 | 9 | 9 | 16 | **SIM** |
| 17 | 17 | 17 | 32 | **SIM** |

- **Custo total:** 51
- **Custo amortizado:** 51/20 = 2.55 ≈ **O(1)** ✓

---

## 5. Comparação dos Três Métodos

| Aspecto | Agregado | Contabilista | Potencial |
|---------|----------|--------------|-----------|
| **Complexidade conceitual** | Simples | Média | Avançada |
| **Intuitividade** | Alta | Alta | Média |
| **Flexibilidade** | Baixa | Média | Alta |
| **Distinção entre operações** | Não | Sim | Sim |
| **Elegância matemática** | Média | Média | Alta |
| **Uso prático** | Análises diretas | Explicações didáticas | Provas formais |

**Quando usar cada um:**

- **Método Agregado:** Quando é fácil calcular o custo total diretamente
- **Método Contabilista:** Quando queremos entender intuitivamente a "economia" de custos
- **Método do Potencial:** Para análises mais complexas e provas formais rigorosas

**Importante:** Todos os três métodos são equivalentes e dão o mesmo resultado!

---

## 6. Outros Exemplos de Estruturas com Análise Amortizada

### Splay Trees
- **Operação:** Splay (rotações para mover nó acessado à raiz)
- **Custo amortizado:** O(log n) por operação
- **Método usado:** Potencial (baseado em ranks)

### Fibonacci Heaps
- **Operações:** Insert, Decrease-Key
- **Custo amortizado:** O(1) para ambas
- **Extract-Min:** O(log n)
- **Método usado:** Potencial (Φ = árvores + 2·nós marcados)

### Union-Find (Disjoint-Set)
- **Com path compression e union by rank**
- **Custo amortizado:** O(α(n)) ≈ O(1) na prática
- **α(n):** função de Ackermann inversa (cresce extremamente lento)

### Table Doubling/Halving
- **Crescimento e encolhimento dinâmico**
- **Custo amortizado:** O(1) com hysteresis adequado

---

## 7. Complexidades - Resumo Geral

### Contador Binário

**Complexidade Temporal:**
- Pior caso (uma operação): O(k)
- Melhor caso (uma operação): O(1)
- **Amortizada (n operações): O(1) por operação**

**Complexidade Espacial:** O(k)

---

### Vetor Dinâmico (Doubling)

**Complexidade Temporal:**
- Pior caso (uma operação): O(n)
- Melhor caso (uma operação): O(1)
- **Amortizada (n operações): O(1) por operação**

**Complexidade Espacial:**
- Total: O(n)
- Overhead: até 2n espaços (fator 2)

---

## 8. Conceitos Importantes

### Diferenças Cruciais

**Análise Amortizada vs. Análise de Caso Médio:**

| Análise Amortizada | Análise de Caso Médio |
|--------------------|-----------------------|
| Não usa probabilidade | Usa probabilidade |
| Pior caso sobre sequências | Média sobre distribuições de entrada |
| Garante desempenho | Assume entradas "típicas" |
| Sempre correta | Depende da distribuição real |

**Por que Análise Amortizada é útil?**

1. **Mais realista:** Reflete melhor o comportamento em sequências de operações
2. **Mais precisa:** Evita pessimismo excessivo da análise de pior caso
3. **Garantias fortes:** Não faz suposições probabilísticas
4. **Prática:** Muitas estruturas reais seguem esse padrão

---

## 9. Dicas para a Apresentação

### Estrutura Recomendada

1. **Introdução (5 min)**
   - Motivação: por que análise de pior caso pode ser pessimista
   - Definição de análise amortizada
   - Diferença com análise de caso médio

2. **Métodos (10-15 min)**
   - Apresentar os três métodos
   - Explicar intuição de cada um
   - Mostrar quando usar cada método

3. **Exemplo 1: Contador Binário (10 min)**
   - Explicar problema
   - Análise ingênua (pior caso)
   - Análise amortizada com 2-3 métodos
   - **EXECUTAR O CÓDIGO** e mostrar resultados

4. **Exemplo 2: Vetor Dinâmico (10 min)**
   - Explicar problema e técnica de doubling
   - Análise amortizada
   - **EXECUTAR O CÓDIGO** e mostrar resultados

5. **Conclusão (5 min)**
   - Resumir conceitos principais
   - Outros exemplos (mencionar brevemente)
   - Importância prática

### Dicas de Apresentação

✓ **Execute os códigos ao vivo** - mostre que realmente funciona  
✓ **Use visualizações** - gráficos ajudam muito a entender  
✓ **Comece pelo método agregado** - é o mais intuitivo  
✓ **Use analogias** - banco (contabilista), energia potencial (física)  
✓ **Explique o "porquê"** - não apenas o "como"  
✓ **Dê exemplos concretos** - números reais, não apenas teoria  
✓ **Relacione com prática** - onde isso aparece em estruturas reais  

### O que Evitar

✗ Ficar só na teoria matemática  
✗ Pular os exemplos práticos  
✗ Não executar código  
✗ Apresentar apenas um método  
✗ Não explicar diferença com caso médio  
✗ Ignorar complexidade espacial  

---

## 10. Perguntas Frequentes

**Q: Análise amortizada é apenas teórica?**  
R: Não! É amplamente usada em estruturas de dados práticas como ArrayList (Java), vector (C++), list (Python).

**Q: Operação individual pode ser cara?**  
R: Sim! Análise amortizada não garante tempo para operação individual, apenas a média sobre sequências.

**Q: Qual método é melhor?**  
R: Depende! Agregado é simples, Contabilista é intuitivo, Potencial é poderoso. Todos são equivalentes.

**Q: Como escolher função potencial?**  
R: Experiência e tentativa. Procure medir "desordem" ou "trabalho futuro" na estrutura.

**Q: Análise amortizada funciona com operações intercaladas?**  
R: Sim, desde que a análise considere todas as operações possíveis na sequência.

---

## 11. Referências

### Livros
1. **Cormen, Leiserson, Rivest, Stein (CLRS)** - "Introduction to Algorithms", Capítulo 17
2. **Kleinberg & Tardos** - "Algorithm Design", Capítulo 17
3. **Sedgewick & Wayne** - "Algorithms", 4ª edição

### Artigos Originais
- **Robert Tarjan (1985)** - "Amortized Computational Complexity"
- Primeiro a formalizar o método do potencial

### Recursos Online
- MIT OCW - "Introduction to Algorithms" (6.006)
- Stanford CS161 - Lecture Notes on Amortized Analysis
- Wikipedia: Amortized Analysis

---

## 12. Material Complementar

### Arquivos Fornecidos

1. **contador_binario.c** - Implementação completa em C
2. **vetor_dinamico.py** - Implementação completa em Python
3. **complexidades_resumo.txt** - Tabela resumida de complexidades
4. **analise_amortizada_exemplos.png** - Gráficos de custo acumulado

### Como Usar no Seminário

**Antes da apresentação:**
- Compile o código C: `gcc contador_binario.c -o contador`
- Teste ambos os códigos
- Prepare os slides com os conceitos principais
- Tenha os códigos abertos para mostrar

**Durante a apresentação:**
- Mostre o código brevemente
- **Execute e mostre os resultados**
- Explique como os resultados confirmam a teoria
- Use os gráficos para visualização

---

## Conclusão

**Análise amortizada** é uma técnica poderosa e prática para analisar algoritmos onde operações caras são compensadas por muitas operações baratas.

**Três métodos equivalentes:**
1. **Agregado:** direto e simples
2. **Contabilista:** intuitivo e didático  
3. **Potencial:** elegante e poderoso

**Aplicações reais:**
- Vetores dinâmicos (ArrayList, vector)
- Tabelas hash com redimensionamento
- Estruturas de busca auto-balanceadas
- Union-Find
- Fibonacci Heaps

**Mensagem final:** Análise amortizada nos permite entender o comportamento real de algoritmos de forma mais precisa que análise de pior caso tradicional, sem perder as garantias matemáticas rigorosas.

---

## Boa apresentação! 🎯

**Lembre-se:**
- Comece com a parte teórica e fundamentos
- Depois mostre, explique e execute os códigos
- Apresente complexidade temporal e espacial
- Use os três métodos (ao menos dois deles)
- Faça conexão com aplicações práticas

**Tempo sugerido: 30-45 minutos**
- 5 min: Introdução
- 10 min: Métodos
- 20 min: Exemplos práticos (código + execução)
- 5 min: Conclusão e outros exemplos

---

**Data de preparação:** Novembro de 2025  
**Material completo para seminário de PAA**