# Calculadora de Folha de Pagamento

Este projeto é uma **calculadora simples de folha de pagamento** feita em Python. O programa calcula o salário bruto, descontos (IR, INSS e outros) e o salário líquido com base no valor da hora e no número de horas trabalhadas.

---

## Funcionalidades

- Calcula o **salário bruto**.
- Calcula o **Imposto de Renda (IR)** de 11%, caso aplicável.
- Calcula o **INSS** de 8%.
- Permite adicionar **outros descontos** em porcentagem.
- Exibe o **salário líquido** após todos os descontos.

---

## Como usar

1. Clone este repositório ou baixe o arquivo `folha_de_pagamento.py`.
2. Execute o script com Python 3:

```bash
python folha_de_pagamento.py
```

3. Siga as instruções no terminal:
   - Digite quanto ganha por hora.
   - Digite o número de horas trabalhadas.
   - Informe se paga Imposto de Renda (Sim/Não).
   - Informe se possui outros descontos além do INSS (Sim/Não). Caso sim, digite a porcentagem.

4. O programa exibirá o detalhamento do salário:

```
+ Salário Bruto : R$ ...
- IR (11%) : R$ ...
- INSS (8%) : R$ ...
- Outros (x%) : R$ ...
= Salário Líquido : R$ ...
```

---

## Exemplo de execução

```text
Digite quanto ganha por hora: 50
Digite o numero de horas trabalhas: 160
Paga Imposto de Renda?
Sim
Recebe algum Desconto Alem do Inss?
Não

+ Salário Bruto : R$ 8000.00
- IR (11%) : R$ 880.00
- INSS (8%) : R$ 640.00
- Outros (Não Possui Outros Descontos) : R$ 0.00
= Salário Liquido : R$ 6480.00
```

---

## Requisitos

- Python 3.x

---

## Licença

Este projeto está licenciado sob a MIT License.
