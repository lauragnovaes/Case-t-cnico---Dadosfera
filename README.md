# Case técnico Dadosfera

## Item 2

O dataset foi baixado em formato jsonl para trabalhar com ele com mais facilidade o Power BI foi utilizado para convertê-lo para csv gerando o arquivo (https://github.com/lauragnovaes/Case-t-cnico---Dadosfera/blob/master/product-search-corpus.csv). A versão gerada pelo Power BI foi uma versão reduzida dos dados iniciais devido ao tamanho muito extenso da base de dados inicial. Esse arquivo foi catalogado na plataforma da Dadosfera (https://app.dadosfera.ai/pt-BR/catalog/data-assets/0ef8692b-8c1c-4805-a637-9103ae9eeee2) como pode ser visto na imagem (https://github.com/lauragnovaes/Case-t-cnico---Dadosfera/blob/master/Upload%20de%20dados%20na%20plataforma.png).


## Item 3

Para gerar separar as features da tabela foi utilizado o ChatGPT. Como há uma limitação na quantidade de dados que a versão gratuita aceita como input foi necessário segmentar o arquivo csv em seções que possam ser aceitas por ele, para tal foi feito um programa em python que fazia essa segmentação (https://github.com/lauragnovaes/Case-t-cnico---Dadosfera/blob/master/linhas_csv.py). A partir dessa divisão foram imputadas as 100 primeiras linhas em partes no ChatGPT utilizando o prompt https://github.com/lauragnovaes/Case-t-cnico---Dadosfera/blob/master/Prompt%20chat%20gpt.txt . Os códigos em json gerados pelo ChatGPT foram colados em um aquivo para gerar https://github.com/lauragnovaes/Case-t-cnico---Dadosfera/blob/master/features_corpus.json . Porém, como o arquivo não foi devidamente importado na plataforma, foi necessário uma última etapa de convertê-lo para csv (https://github.com/lauragnovaes/Case-t-cnico---Dadosfera/blob/master/feature-products-corpus.csv) novamente com o auxílio do Power BI. Esse arquivo foi importado no catálogo da plataforma (https://app.dadosfera.ai/pt-BR/catalog/data-assets/ece9fa77-cf7e-4572-914e-87de7ba9f115).

## Item 4

Para análisar os itens por categoria foram realizadas duas análises através de uma consulta em SQL uma para todas as categorias (https://metabase-treinamentos.dadosfera.ai/question/474-produtos-por-categoria) e outra para as 10 maiores categorias (https://metabase-treinamentos.dadosfera.ai/question/476-top-10-maiores-categorias). Com esses dados foi criado o seguinte dashboard: https://github.com/lauragnovaes/Case-t-cnico---Dadosfera/blob/master/Dashboard%20an%C3%A1lise%20de%20produtos.png (https://metabase-treinamentos.dadosfera.ai/dashboard/59-analise-de-produtos-corpus).