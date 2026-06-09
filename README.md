# SERS Mission Control AI

Sistema inteligente de monitoramento de energia renovável em uma missão espacial experimental.

Projeto desenvolvido para a **Global Solution - Soluções em Energias Renováveis e Sustentáveis (SERS)**.

## 1. Descrição do Projeto

O **SERS Mission Control AI** é uma solução computacional em Python criada para simular o monitoramento operacional de uma missão espacial experimental.

O sistema recebe dados simulados de diferentes ciclos da missão e analisa automaticamente:

- Temperatura dos módulos;
- Qualidade da comunicação orbital;
- Nível da bateria principal;
- Geração de energia solar renovável;
- Consumo energético dos módulos;
- Estabilidade operacional;
- Índice de sustentabilidade energética.

A partir dessas informações, o programa classifica os riscos, gera alertas automáticos e recomenda ações básicas para preservar a operação da missão e melhorar o uso de energia renovável.

## 2. Problema Proposto

Em missões espaciais, o uso eficiente de energia é essencial para manter os sistemas funcionando com segurança. Como a captação de energia solar pode variar durante a operação, é importante monitorar geração, consumo, bateria e estabilidade dos módulos.

Este projeto simula um sistema de controle capaz de identificar situações críticas, como baixa geração solar, consumo excessivo, superaquecimento, falhas de comunicação e queda de estabilidade operacional.

## 3. Objetivo

Desenvolver uma solução de monitoramento inteligente para analisar dados simulados de sistemas energéticos de uma missão espacial experimental, aplicando conceitos de:

- Energia;
- Potência e consumo;
- Energia solar renovável;
- Sustentabilidade;
- Algoritmos;
- Estruturas condicionais;
- Tomada de decisão automatizada.

## 4. Funcionalidades

### Monitoramento de Dados Simulados

O programa interpreta dados simulados da missão em ciclos operacionais. Cada ciclo possui informações sobre temperatura, comunicação, bateria, geração solar, consumo de energia e estabilidade.

### Geração Automática de Alertas

Cada módulo é classificado automaticamente como:

- `NORMAL`
- `ATENCAO`
- `CRITICO`

Esses alertas indicam o nível de risco de cada área monitorada.

### Tomada de Decisão Básica

Com base nos alertas identificados, o sistema gera recomendações automáticas, como:

- Acionar protocolo emergencial;
- Reduzir cargas não essenciais;
- Priorizar módulos essenciais;
- Ajustar o uso da energia renovável;
- Intensificar o monitoramento.

### Índice de Sustentabilidade Energética

O sistema calcula um índice de sustentabilidade com base na relação entre geração solar e consumo energético:

```text
Índice de Sustentabilidade = (Geração Solar / Consumo Energético) * 100
```

Quanto maior o índice, melhor o aproveitamento da energia renovável em relação ao consumo da missão.

### Visualização Simplificada dos Dados

O sistema exibe um painel no terminal com:

- Dados de cada ciclo;
- Status dos módulos;
- Barras visuais simples;
- Pontuação de risco;
- Recomendação automatizada;
- Relatório final da missão.

## 5. Tecnologias Utilizadas

- Python 3
- Estruturas condicionais
- Laços de repetição
- Listas
- Funções
- Simulação de dados
- Lógica de tomada de decisão

## 6. Estrutura do Projeto

```text
sers-mission-control-ai/
├── sers_mission_control.py
├── exemplo_saida.txt
├── entrega.txt
└── README.md
```

## 7. Como Executar

### Pré-requisito

Ter o Python 3 instalado no computador.

### Passo a passo

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/sers-mission-control-ai.git
```

Acesse a pasta do projeto:

```bash
cd sers-mission-control-ai
```

Execute o programa:

```bash
python sers_mission_control.py
```

Ou, em alguns sistemas:

```bash
python3 sers_mission_control.py
```

## 8. Exemplo de Dados Simulados

Cada ciclo da missão segue a estrutura abaixo:

```python
[temperatura, comunicacao, bateria, geracao_solar, consumo_energia, estabilidade]
```

Exemplo:

```python
[33, 61, 53, 45, 82, 67]
```

Esse ciclo representa:

- Temperatura: 33°C;
- Comunicação: 61%;
- Bateria: 53%;
- Geração solar: 45 kWh;
- Consumo energético: 82 kWh;
- Estabilidade: 67%.

## 9. Critérios de Avaliação Atendidos

### Técnica

O projeto possui código organizado em funções, análise de múltiplos indicadores, geração de alertas, classificação de risco e relatório final.

### Inovação

A solução adiciona um índice de sustentabilidade energética, análise de geração solar renovável e recomendações automáticas para economia de energia em uma missão espacial.

### Usabilidade

A saída no terminal foi organizada em formato de painel, com textos claros, classificação por status e barras visuais simples para facilitar a leitura.

### Apresentação

O sistema apresenta os resultados de forma objetiva, mostrando os riscos da missão, a área mais afetada e o impacto potencial da solução.

## 10. Possíveis Melhorias Futuras

- Criar interface gráfica;
- Salvar relatórios em arquivo CSV;
- Gerar gráficos com bibliotecas Python;
- Integrar sensores reais ou APIs de simulação;
- Utilizar aprendizado de máquina para prever falhas futuras.

## 11. Integrantes

- Julia Nunes Frederici
- Maria Beatriz
- Rafael Rafael Rebello
