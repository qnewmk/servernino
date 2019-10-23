from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['dbskills']



#Criando ou conectando a uma collection
#collection = db['skillsCollection']

# print(db.command('serverStatus'))



#Estrutura do banco no mongo db
teste={"HCM":[{"CSA":[{"Nino":"Bien","Victor":"Bien","kaio":"Intermediario"}]},{"OO":[{"Nino":"Bien","Victor":"Bien","kaio":"Intermediario"}]}]}
#ADD Pilar
def add_pilar(colecao,inser):
	collection = db[f'{colecao}']
	if inser != "":
		collection.insert_one(inser)
	else:
		collection.insert_one({"default":"input","teste":{"teste dentro":"testado dentro","teste dentro2":"testado dentro","teste dentro3":{"teste dentro dentro":"muito dentro bem loko "}}})
client.close()

if __name__ == '__main__':
	#Teste tem que ser passado como parametro pelo site que ele for chamado. O parametro é o nome da collection 
	#que será criada no banco, ou seja, tem que ser um nome que não se repita ou então, o banco pode ao invéz
	#de criar a collection, simplesmente adicionar seja lá o que for na sua collection.
	add_pilar("ITOM",teste)
