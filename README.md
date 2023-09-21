# Recorde de temperaturas (2012-2021) em comparação com 2022
### Descrição
Esse é um projeto com intuito de projetar as amplitudes térmicas divulgadas pela National Centers for Environmental Information (NCEI), os dados utilizados foram coletados pela estação climática do Aeroporto Internacional de São Francisco (EUA). Nesse trabalho foram analisadas as amplitudes térmicas dos 365 dias do ano, em um recorte de dez anos (2012-2021), para encontrar as maiores e menores temperaturas registradas no período e compará-las com o ano de 2022, indicando as marcas  do ano que se sobressairam diante o histórico da década. 

### Inspiração
A motivação para esse trabalho deu-se ao encontrar um exercício do Coursera sobre plots utilizando a biblioteca matplotlib. O exercício proposto tinha as mesmas características, entretanto, o dataframe disponibilizado eram de estações no entrono de Detroit (EUA).

### Objetivo
Inicialmente, o objetivo era de realizar essa análise com dados da cidade de São Paulo, já que no NCEI estão disponibilizadas as temperaturas de milhares de estações climáticas espalhadas por todo mundo, no entanto devido a falta de atualizações da base de dados (a maioria dos datasets disponíveis tinham as últimas observações datadas de 1990), e longos períodos com ausência de dados.

### Manipulação dos dados
O projeto foi desenvolvido no Google Colab. A partir do download do dataset com as temperaturas do aeroporto no site da NCEI, foi feita a limpeza da base dados, recortando o frame do período de estudo, removendo as variáveis que não são utilizadas e as observações dos anos bissextos (29/02) no período.  

Também é feita a conversão de decimais de grau para graus Celsius das temperaturas máximas e mínimas, além de aplicar a função para obter o dia do ano armazenando na coluna 'DAY OF YEAR', a qual será a variável de agrupamento dos dias.

Dividimos o dataframe em dois, baseado em temperatura máxima e mínima, em seguida novamente separamos agora observando o ano da amostragem, para conseguirmos agrupar pelos dias do ano os extremos de temperatura registrados em cada um deles.

### Plot

### Referências
https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily
https://www.coursera.org/learn/python-plotting/peer/QjMGl/plotting-weather-patterns
