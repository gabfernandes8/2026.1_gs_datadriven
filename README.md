<h1 align="center"> Global Solution </h1>
<p align="center"> Monitoramento de Atividade Vulcânica via Satélite </p>

<br>

## 🤔 sobre o projeto
Este sistema em Python foi criado como parte da avaliação Global Solution do primeiro semestre de 2026, para a disciplina de Data Driven Application e Data Science. O projeto simula um centro de controle que processa dados de sensores orbitais para monitorar vulcões ativos. Ele permite registrar erupções e emissões de gases em escala global. A aplicação se concentra em transformar medições brutas de sensores infravermelhos e térmicos em relatórios úteis para segurança civil e monitoramento geológico.
<br>
<br>


## 💻 funcionalidades

### Gerenciamento de Dados
* **Entrada Flexível:** O usuário define a volumetria de eventos a serem analisados por sessão.
* **Validação de Integridade:**
    * Implementação de filtros para garantir que a **área afetada** seja estritamente positiva ($> 0$).
    * Restrição de **intensidade** via escala paramétrica (1 a 10) para evitar outliers.
* **Estrutura Paralela:** Organização de dados em múltiplas listas para garantir a rastreabilidade de tipos, localizações e métricas.

### Processamento e Análise Estatística
* **Agregadores Totais:** Cálculo automatizado da área total impactada e contagem global de registros.
* **Métricas de Tendência Central:** Processamento da média de intensidade dos eventos para fins de comparação.
* **Análise de Frequência:** Identificação da região geográfica com maior densidade de ocorrências detectadas.
* **Cálculo de Densidade:** Algoritmo para determinar a relação ocorrências/km².

### Inteligência de Negócio e Criticidade
* **Filtro de Anomalias:** Identificação automática de eventos que operam acima da média de gravidade do dataset.
* **Identificação do Evento Crítico:** Algoritmo de priorização que cruza os dados de **maior intensidade** e **maior extensão territorial** para destacar o risco máximo.

### Relatório
* Geração de relatório formatado contendo o resumo geral, análises detalhadas e o local completo do evento mais relevante para suporte à decisão.

<div>

</div>


<br>


## 👥 integrantes:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/gabfernandes8">
        <img src="https://avatars.githubusercontent.com/gabfernandes8" width="100px;" alt="Foto de Gabriela Fernandes no GitHub"/><br>
        <sub>
          <b>Gabriela Fernandes</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/furiatee">
        <img src="https://avatars.githubusercontent.com/furiatee" width="100px;" alt="Foto de Júlia Furiate no GitHub"/><br>
        <sub>
          <b>Júlia Furiate</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/viliaaivil">
        <img src="https://avatars.githubusercontent.com/viliaaivil" width="100px;" alt="Foto de Livia Santos no GitHub"/><br>
        <sub>
          <b>Lívia Santos</b>
        </sub>
      </a>
    </td>
  </tr>   
</table>
