import json
from infos.Summoner import Summoner
from infos.Champions import Champions
data = open('commande.json')
commande=json.load(data)

def parse(req):
    reqCom = req.split(':')[0]
    key=[]
    for com in commande:
        for comKey in com:
            key.append(comKey)
    if reqCom in key:
        match reqCom:
            case 'champ':
                return Champions.allKit(req)
    else:
        return Summoner.sum(req)
    