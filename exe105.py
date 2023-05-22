# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um 
# dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as docstrings da função.

def notas(*notas, situacao = False):
    """
     Esta função calcula o número de notas, a nota mais alta, mais baixa e média de um aluno e sua situação
     de acordo com sua nota média.
    
     Argumentos:
         *notas: Um número variável de valores representando as notas do aluno.
         situacao: Um valor booleano que indica o status dos alunos com base na média.
        
     Retorna:
         Um dicionário contendo as seguintes chaves:
         - 'qtd notas': O número de notas.
         - 'nota maior': A nota mais alta.
         - 'nota menor': A nota mais baixa.
         - 'nota media': A média das notas.
         - 'situacao' (opcional): Situação dos alunos com base na média. Presente somente se `situacao` for True.
     """
    aluno = {}
    aluno['qtd notas']  = len(notas)
    aluno['nota maior'] = max(notas)
    aluno['nota menor'] = min(notas)
    aluno['nota media'] = sum(notas)/len(notas)
    if situacao:
        if aluno['nota media'] > 7:
            aluno['situacao'] = 'Boa'
        elif aluno['nota media'] < 5:
            aluno['situacao'] = 'Ruim'
        else:
            aluno['situacao'] = 'Razoável'
    return aluno
            
n = notas(8.9, 2.5, 1, 10, situacao=True)
print(n)
help(notas)

# Resolução do professor

def notas(*n, sit = True):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (quantidade variável de valores)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionario com várias informações sobre a situação da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Boa'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoável'
        else:
            r['situacao'] = 'Ruim'
    return r

resp = notas(9, 10, 5.5, sit=True)
print(resp)