# igrejas
dados sobre instituicoes religiosas registradas no brasil

## Arquivos
- `relatorio.ipynb` - arquivo principal com as análises
- `cbr.db` banco contendo os dados geográficos extraidos do IBGE;
- `mod.csv` dados gerado com dados intermediários das instituições;
- `per_latlon.csv` dados gerados pela associação de mod.csv com os dados do IBGE;
- `religiao.db` base de dados com todos os cnaes **94.91-0-00** do Brasil

## Uso
- depois de instalar o jupyter notebook;
- `pip install -r requirements.txt`;
- renderizar o notebook

## API graphql
- executar `python api/api.py`
- acessar `http://localhost:5000/graphql` e aplicar as queries
