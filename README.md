# Sistema de Gerenciamento de Componentes Eletrônicos

```python
Interface de Linha de Comando para cadastro e consulta de componentes eletrônicos passivos, com validação de parâmetros físicos e cálculo de impedância em um circuito em série.
```

![Banner](/assets/wallpaper.jpg)

## Funcionalidades

- Cadastro de **resistores**, **capacitores** e **indutores**
- Validação de grandezas físicas com valores numéricos e positivos
- Verificação da **tensão máxima** do componente em relação à tensão do circuito
- Listagem dos componentes cadastrados
- Cálculo da impedância individual de cada componente
- Cálculo da impedância total estimada do circuito em série
- Representação textual simples da topologia do circuito

## Estrutura do projeto

![estrutura-pastas](/assets/estrutura-pastas.png)

- `cli.py` — interface com o usuário
- `app.py` — regras de negócio e fluxo de cadastro/listagem
- `models.py` — classes de domínio e validações

## Como funciona

Ao iniciar a aplicação, o usuário informa a tensão nominal do circuito.  
Em seguida, pode:

- adicionar resistores
- adicionar capacitores
- adicionar indutores
- listar os componentes cadastrados e calcular suas impedâncias
- encerrar o sistema

Cada componente possui:

- nome
- fabricante
- tensão máxima
- grandeza específica:
  - resistência, no caso de resistor
  - capacitância, no caso de capacitor
  - indutância, no caso de indutor

## Regras de validação

O sistema impede o cadastro de dados inválidos:

- tensão do circuito deve ser maior que zero
- tensão máxima do componente deve ser maior ou igual à tensão do circuito
- resistência, capacitância e indutância devem ser números positivos
- frequência informada para cálculo deve ser numérica

## Cálculo de impedância

O comportamento dos componentes segue estas regras:

- **Resistor**: impedância igual ao valor da resistência
- **Capacitor**:  
  A reatância capacitiva é calculada como:
1 dividido por (2 vezes pi vezes a frequência vezes a capacitância).
Em outras palavras:
quanto maior a frequência ou a capacitância, menor será a impedância.
Caso a frequência seja zero (corrente contínua), o capacitor se comporta como um circuito aberto, ou seja, a impedância tende a um valor muito alto.
- **Indutor**:  
  A reatância indutiva é calculada como:
2 vezes pi vezes a frequência vezes a indutância.
Ou seja:
quanto maior a frequência ou a indutância, maior será a impedância.

A impedância total exibida é uma **soma linear das magnitudes**, usada como cálculo escalar simplificado.