## Apache Beam - manipulação de dataframes 

Aprendemos a utilizar o Apache Beam para realizar a ingestão de dados, onde utilizamos o ReadFromText para fazer a leitura dos dois datasets, dos dois dados brutos, tanto de casos de dengue quanto de precipitação meteorológica, o dataset de chuvas.

Aplicamos nesses datasets várias transformações, como os Maps, FlatMap, Filter, também agrupamos e também combinamos esses dados aplicando as transformações necessárias para deixar o dado da forma como planejarmos no início, para ser utilizado depois numa persistência de dados, onde fizemos a escrita desses dados utilizando o WriteToText.

E a partir daí pegamos esses dados persistidos em um arquivo CSV e o analisamos em um data frame Pandas.

A trazer o Apache Beam aqui para dentro do nosso ambiente, do nosso código Python, além de realizar a instalação dele dentro do nosso ambiente virtual e começamos realizando a ingestão dos dados com o método ReadFromText, onde utilizamos tanto na pipeline de dengue quanto na pipeline de chuvas.

Na pipeline de dengue nós realizamos a leitura do dado bruto de casos de dengue, para o delimitador pipe, várias colunas que nós acabamos fazendo vários processamentos. E na pipeline de chuvas lemos o dado bruto de chuvas.csv, com várias informações do mesmo dia sobre a quantidade de chuvas nos estados.

Aplicamos nesses datasets várias transformações, como o Map, aplicamos também aqui FlatMap, agrupamos pela chave, fizemos combinações por chave e também aplicamos depois no resultado a união de duas pipelines diferentes, de chuvas e de dengue, depois de seus respectivos tratamentos, fizemos o merge, as juntamos. Aplicamos também filtros e depois preparamos para escrita.

Após a preparação para escrita criamos um header, que seria o header do nosso arquivo do tipo CSV, já que persistimos o nosso dado em um arquivo do tipo texto com o CSV, então para isso utilizamos também um método do Apache Beam, da nossa SDK, que é o WriteToText, onde passamos o nome do nosso arquivo, o tipo, que é o sufixo, e o header dele, já que é um CSV que é bem importante.

E com isso criamos o resultado, que é esse arquivo do tipo CSV, separado, por ponto e vírgula. E após consolidar todo o resultado dos tratamentos dos processos, desde a análise que nós fizemos, o trouxemos para um ambiente bem conhecido dos cientistas de dados, que é o Jupyter Notebook.

Importamos o Pandas e pelo Pandas fizemos a leitura de um arquivo do tipo CSV, que foi transformado em um data frame, passamos o arquivo e o delimitador específico.

E com o Pandas, nós aplicamos aqui um método específico, como, por exemplo, o groupby, para realizar algum tipo de processamento, para verificar as correlações entre a quantidade de chuva, a precipitação meteorológica, e a quantidade casos de dengue.


Opções da pipeline e leitura de dados:
https://beam.apache.org/documentation/patterns/pipeline-options/

ReadFromText:
https://beam.apache.org/releases/pydoc/2.6.0/apache_beam.io.textio.html

Apache beam Map:
https://beam.apache.org/documentation/transforms/python/elementwise/map/

PCollection characteristics:
https://beam.apache.org/documentation/programming-guide/#pcollection-characteristics

Lambda expression:
https://docs.python.org/pt-br/3/tutorial/controlflow.html#lambda-expressions

GroupByKey:
https://beam.apache.org/documentation/transforms/python/aggregation/groupbykey/

Flaten (merge Pcollection):
https://beam.apache.org/documentation/programming-guide/#flatten

CoGroupByKey:
https://beam.apache.org/documentation/transforms/java/aggregation/cogroupbykey/ 
  
source env-beam/bin/activate
