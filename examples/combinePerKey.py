'''O método criado utiliza o sum() para somar os valores pela chave, porém, ele está dentro de outro método do python, o min(). Este retorna sempre o menor valor que for passado por parâmetro para ele. Então o valor que vai ser resultante do processo sempre será o valor 5 ou menor. Já que este é o valor que ele compara para resultar em sua saída. 
No exemplo, o valor do total de soma da chave 'B' é de 10, por tanto, a saída do método min(10, 5) será 5. Já nas chaves A e C o resultado da soma dos valores das chaves é 4, sendo este menor que 5, a saída será o valor 4.
'''

import apache_beam as beam

def saida_maxima(elementos):
    valor_saida_maxima = 5
    return min(sum(elementos), valor_saida_maxima)

pipeline = beam.Pipeline()
plants = (
    pipeline
    | 'Lista de números' >> beam.Create([
        ("A", 2),
        ("B", 7),
        ("B", 3),
        ("A", 1),
        ("C", 4),
        ("A", 1),
    ])
    | 'Tirar da lista com gerador' >> beam.CombinePerKey(saida_maxima)
    | beam.Map(print))

pipeline.run()