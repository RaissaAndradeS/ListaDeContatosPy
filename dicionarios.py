dados = {"nome":"raissa", 
         "sobrenome": "andrade",
         "idade": "25",
         "ex": ["doido", "maluco", "ateu"],
         "filhos":[{"nome": "jose", "idade": "2"}, {"nome": "raul", "idade": "1"}]
        }

nome = dados["nome"]

print(nome)

print(dados["filhos"][0]["idade"])