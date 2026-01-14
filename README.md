☕ Data Pipeline: Monitoramento Agroclimático Estratégico (Lavras/MG)
📝 Visão Geral
Este projeto foi desenvolvido como um estudo prático de Engenharia de Dados, focado na construção de uma pipeline ponta a ponta (End-to-End). O sistema automatiza a coleta de dados climáticos para a região de Lavras/MG, processa indicadores agronômicos e disponibiliza alertas críticos para a cafeicultura em um dashboard interativo.

🏗️ Arquitetura e Engenharia de Dados
O projeto prioriza a modularidade e a integridade do fluxo de dados:

Ingestão de Dados: Script Python para extração de dados em tempo real via API OpenWeather.

ETL (Extração, Transformação e Carga): Utilização da biblioteca Pandas para limpeza, padronização e estruturação dos dados brutos em séries temporais prontas para análise.

Feature Engineering (Regras de Negócio): Implementação de algoritmos baseados em pesquisas agronômicas e suporte de IA para monitoramento de riscos:

Risco de Ferrugem: Identificação de janelas climáticas favoráveis ao fungo (cruzamento de umidade >80% e faixas térmicas ideais).

Estresse Térmico: Detecção de picos de temperatura (>30°C) prejudiciais à fisiologia do café arábica.

🤖 Orquestração e Automação
A autonomia do sistema é garantida por um processo de orquestração:

Orquestrador (run_etl.py): Script central que coordena a execução da pipeline e realiza verificações de qualidade.

Agendamento Automático: Integração com o Windows Task Scheduler para disparar a pipeline de forma independente 3x ao dia (06h, 14h, 22h).

📊 Visualização de Dados (BI)
Os dados processados alimentam um dashboard no Power BI, focado em suporte à decisão:

KPIs de Alerta: Identificação visual imediata de eventos críticos na lavoura.

Tendência Temporal: Análise histórica da temperatura média para planejamento de manejo.

⚙️ Configuração do Ambiente
Clone o repositório.

Instale as dependências: pip install -r requirements.txt

Gere o histórico inicial: python -m src.backfill

O dashboard está disponível na pasta /dashboard.

Nota: Ao abrir o Power BI pela primeira vez, atualize o caminho do arquivo fonte (CSV) para a sua pasta local.

🧠 Problemas Reais Solucionados
Monitoramento Contínuo: Substituição da coleta manual de dados por uma pipeline automatizada 24/7.

Economia no Campo: O alerta de ferrugem auxilia na aplicação assertiva de defensivos, evitando desperdícios.

Saúde da Planta: Identificação precisa de estresse térmico, permitindo ajustes rápidos no manejo hídrico ou sombreamento.
