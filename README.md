☕ Data Pipeline: Monitoramento Agroclimático Estratégico (Lavras/MG)
📝 Visão Geral
Este projeto implementa uma pipeline de dados End-to-End para monitoramento de variáveis climáticas críticas na cafeicultura de Lavras/MG. O sistema automatiza a ingestão de dados, aplica lógica de Feature Engineering para detecção de riscos biológicos e visualiza insights estratégicos em um dashboard profissional.

🏗️ Arquitetura e Engenharia de Dados
O projeto foi desenvolvido com foco em modularidade e automação de processos:

Ingestão de Dados: Extração automatizada via API climática utilizando Python.

Pipeline de Transformação (ETL): Processamento de dados brutos com Pandas para limpeza, normalização de tipos e estruturação de séries temporais.

Feature Engineering: Implementação de lógica algorítmica para monitoramento de riscos agronômicos:

Risco de Ferrugem: Identificação de janelas de alta umidade (>80%) e temperatura ideal para o fungo.

Estresse Térmico: Monitoramento de picos térmicos prejudiciais à produtividade do café arábica (>30°C).

🤖 Orquestração e Automação
O diferencial técnico deste projeto é a sua autonomia operacional:

Orquestrador (run_etl.py): Script central que coordena a execução da pipeline de dados e o controle de qualidade.

Agendamento Automático: Utilização do Windows Task Scheduler para disparar a pipeline 3x ao dia (06h, 14h, 22h), garantindo dados atualizados nos horários críticos de manejo.

Data Quality: Verificação automática da integridade dos dados antes da carga final no dashboard.

📊 Business Intelligence
O dashboard no Power BI reflete o resultado da engenharia de dados através de:

KPIs de Alerta Semânticos: Identificação visual imediata de eventos críticos.

Tendência Temporal: Análise da variação térmica média para suporte à decisão agronômica.

⚙️ Configuração
Instale as dependências: pip install -r requirements.txt

Execute o script de histórico: python -m src.backfill

Agende o run_etl.py para automação contínua.

🧠 Problemas Reais que esta Engenharia resolve:
Eliminação de Erros Manuais: A automação via Agendador de Tarefas e o orquestrador run_etl.py eliminam a necessidade de intervenção humana, garantindo que o dado esteja sempre disponível e correto.

Manejo Preventivo de Doenças: O algoritmo de risco de ferrugem permite que o produtor aplique defensivos apenas quando as condições climáticas favorecem o fungo, gerando economia e sustentabilidade.

Proteção de Produtividade: A detecção de estresse térmico responde se a planta parou de produzir devido ao calor excessivo, permitindo ajustes no manejo hídrico.

Confiabilidade do Dado: Ao separar a pipeline da visualização e incluir verificações de qualidade, o sistema garante que o tomador de decisão nunca baseie suas ações em dados corrompidos ou em escalas erradas.
