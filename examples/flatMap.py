import apache_beam as beam

def gera_elementos(elementos):
    for elemento in elementos:
        yield elemento

with beam.Pipeline() as pipeline:
    plants = (
        pipeline
        | 'Lista de números' >> beam.Create([
            [2, 1, 6],
            [5, 3],
        ])
        | 'Tirar da lista com gerador' >> beam.FlatMap(gera_elementos)
        | beam.Map(print))
    
    '''
    Utilizar o FlatMap para criar geradores é algo bem comum na engenharia de dados. Para entender melhor como utilizar essa ferramenta nos seus próximos projetos, a seguir, você encontra o exemplo de uma pipeline que recebe 2 listas de diferentes tamanhos, e que ao final apresenta uma pcollection com apenas 1 item da lista por elemento.
    '''