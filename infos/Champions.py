from riot import lol_watcher
import discord,requests

class Champions:
    def allKit(req):
        champ= req.split(':')[1]
        dataChamp= Champions.getData(champ)
        icon= "https://cdn.communitydragon.org/latest/champion/"+str(dataChamp['id'])+"/square"
        key=['Q','W','E','R','P']
        embedAll=[]
        passif = dataChamp['passive']
        embedP=Champions.passif(passif,icon,champ,dataChamp)
        embedAll.append(embedP)
        for i in range(4):
            spells = dataChamp['spells'][i]
            embedItem=Champions.spell(spells,icon,champ,key[i],dataChamp)
            embedAll.append(embedItem)
        
        return embedAll
    
    def spell(spell,icon,champ,key,data):
        embed= discord.Embed(title=spell['name'],description=spell['description'],color=0x0099ff)
        embed.set_author(name=champ+" "+key,icon_url=icon)
        embed.set_thumbnail(url="https://cdn.communitydragon.org/latest/champion/"+str(data['id'])+"/ability-icon/"+str(key.lower()))
        #gestion cout/lvl
        if spell['costCoefficients'][0]!=spell['costCoefficients'][1] : 
            cout= str(spell['costCoefficients'][0])+"/"+str(spell['costCoefficients'][1])+"/"+str(spell['costCoefficients'][2])+"/"+str(spell['costCoefficients'][3])+"/"+str(spell['costCoefficients'][4])
            if key == 'R':
                cout=str(spell['costCoefficients'][0])+"/"+str(spell['costCoefficients'][1])+"/"+str(spell['costCoefficients'][2])
            embed.add_field(name='Coût en Ressource :',value=cout)
        else:
            if spell['costCoefficients'][0]==0.0:
                embed.add_field(name='Pas de Coût',value='')
            else:
                embed.add_field(name='Coût en Ressource :',value=spell['costCoefficients'][0])
                
        #gestion cd/lvl
        if spell['ammo']['ammoRechargeTime'][0]!=0:
            if spell['cooldownCoefficients'][0]!=0:
                cooldown = str(spell['cooldownCoefficients'][0])+"/"+str(spell['cooldownCoefficients'][1])+"/"+str(spell['cooldownCoefficients'][2])+"/"+str(spell['cooldownCoefficients'][3])+"/"+str(spell['cooldownCoefficients'][4])
                charge = str(spell['ammo']['ammoRechargeTime'][0])+"/"+str(spell['ammo']['ammoRechargeTime'][1])+"/"+str(spell['ammo']['ammoRechargeTime'][2])+"/"+str(spell['ammo']['ammoRechargeTime'][3])+"/"+str(spell['ammo']['ammoRechargeTime'][4])
                
                if key=='R':
                    cooldown = str(spell['cooldownCoefficients'][0])+"/"+str(spell['cooldownCoefficients'][1])+"/"+str(spell['cooldownCoefficients'][2])
                    charge=str(spell['ammo']['ammoRechargeTime'][0])+"/"+str(spell['ammo']['ammoRechargeTime'][1])+"/"+str(spell['ammo']['ammoRechargeTime'][2])
                if spell['cooldownCoefficients'][0]==spell['cooldownCoefficients'][1]:
                    cooldown = str(spell['cooldownCoefficients'][0])
                if spell['ammo']['ammoRechargeTime'][0] == spell['ammo']['ammoRechargeTime'][1]:
                    charge = str(spell['ammo']['ammoRechargeTime'][0])         
                embed.add_field(name='Délai entre charge :',value=cooldown)
                embed.add_field(name='Délai de Rechargement :',value=charge)
            else:
                cooldown= str(spell['ammo']['ammoRechargeTime'][0])+"/"+str(spell['ammo']['ammoRechargeTime'][1])+"/"+str(spell['ammo']['ammoRechargeTime'][2])+"/"+str(spell['ammo']['ammoRechargeTime'][3])+"/"+str(spell['ammo']['ammoRechargeTime'][4])
                if key=='R':
                    cooldown=str(spell['ammo']['ammoRechargeTime'][0])+"/"+str(spell['ammo']['ammoRechargeTime'][1])+"/"+str(spell['ammo']['ammoRechargeTime'][2])
                if spell['ammo']['ammoRechargeTime'][0]==spell['ammo']['ammoRechargeTime'][1]:
                    cooldown= str(spell['ammo']['ammoRechargeTime'][0])
                embed.add_field(name='Délai de Rechargement :',value=cooldown)
        else:
            if spell['cooldownCoefficients'][0]==0:
                embed.add_field(name='Pas de Rechargement',value='')
            else:
                cooldown = str(spell['cooldownCoefficients'][0])+"/"+str(spell['cooldownCoefficients'][1])+"/"+str(spell['cooldownCoefficients'][2])+"/"+str(spell['cooldownCoefficients'][3])+"/"+str(spell['cooldownCoefficients'][4])
                if key=='R':
                    cooldown = str(spell['cooldownCoefficients'][0])+"/"+str(spell['cooldownCoefficients'][1])+"/"+str(spell['cooldownCoefficients'][2])
                if spell['cooldownCoefficients'][0]==spell['cooldownCoefficients'][1]:
                    cooldown = str(spell['cooldownCoefficients'][0])
                embed.add_field(name='Délai de Rechargement :',value=cooldown)
        return embed

    def passif(passif,icon,champ,data):
        embed= discord.Embed(title=passif['name'],description=passif['description'],color=0x0099ff)
        embed.set_author(name=champ+' P',icon_url=icon)
        embed.set_thumbnail(url="https://cdn.communitydragon.org/latest/champion/"+str(data['id'])+"/ability-icon/passive")
        return embed
    
    def getData(champ):
        idChamp=''
        listeChamp = requests.get("https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/fr_fr/v1/champion-summary.json").json()
        for lChamp in listeChamp:
            if(lChamp['name']==champ):
               idChamp=lChamp['id']
        dataChamp= requests.get("https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/fr_fr/v1/champions/"+str(idChamp)+".json").json()
        return dataChamp
