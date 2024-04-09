"""1.Uma escola precisa de um software que calcule a 
média de alunos. 
Para isso o software deve receber o nome e três 
notas dos alunos. Com estes dados o software deve imprimir:
| ---------------------------------- | 
| Média	    | Imprimir               | 
| ---------------------------------- | 
| ==10	    | Aprovado com Distinção |
| >=7	    | Aprovado!              |
| >=5   	| Em exame               |
| <5	    | Reprovado              |
| ---------------------------------- | 
"""

nome=str(input('Digite o nome do aluno:')).capitalize()
matricula=int(input('Digite a matricula'))
nota1=float(input('Digite a primeira nota'))
nota2=float(input('Digite a segunda nota'))
nota3=float(input('Digite a terceira nota'))
media= (nota1 + nota2 + nota3) / 3

if media ==10:
    print(f'Aprovado com distinção')
elif media >= 7:
    print(f'Aprovado')
elif media >=5:
    print(f'Em exame')
else:
    print(f'Reprovado')
print(f'Media final do aluno {nome} - {matricula}: {media}')
