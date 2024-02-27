aluno = {
    'nome': input('Nome: '),
    'media': float(input('Média: '))
}

if aluno['media'] >= 60:
    aluno['sf'] = 'AP'
else:
    aluno['sf'] = 'RP'

print(aluno)
