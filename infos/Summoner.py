from riot import lol_watcher
import discord,requests
class Summoner:
      def sum(req):
        data = lol_watcher.summoner.by_name("euw1", req)
        ranked = lol_watcher.league.by_summoner('euw1', data['id'])
        # matchList = Summoner.mostPlayed(data)
        
        icon='https://ddragon.leagueoflegends.com/cdn/14.2.1/img/profileicon/'+str(data['profileIconId'])+'.png'
        embed = discord.Embed(title=data['name'],description="Lvl "+str(data['summonerLevel']),color=0x0099ff)
        embed.set_thumbnail(url=icon)
        # print(len(ranked))
        if not not(ranked):
          if ranked[0]['queueType']=='RANKED_FLEX_SR':
            rankFlex = str(ranked[0]['tier'])+" "+str(ranked[0]['rank'])+" "+str(ranked[0]['leaguePoints'])+" LP"
            embed.add_field(name='Flex: ',value=rankFlex)
            if len(ranked)==2:
              rankSolo = str(ranked[1]['tier'])+" "+str(ranked[1]['rank'])+" "+str(ranked[1]['leaguePoints'])+" LP"
              embed.add_field(name='Solo: ',value=rankSolo)
            else:
              embed.add_field(name='Pas de ranked Solo',value='')

          else:
            rankSolo = str(ranked[0]['tier'])+" "+str(ranked[0]['rank'])+" "+str(ranked[0]['leaguePoints'])+" LP"
            embed.add_field(name='Solo: ',value=rankSolo)
            if len(ranked)==2:
              rankFlex = str(ranked[1]['tier'])+" "+str(ranked[1]['rank'])+" "+str(ranked[1]['leaguePoints'])+" LP"
              embed.add_field(name='Flex: ',value=rankFlex)
            else:
              embed.add_field(name='Pas de ranked Flex',value='')

        else:
          embed.add_field(name='Pas de ranked sur ce compte',value='')
        return embed
      
      def mostPlayed(data):
        d={}
        matchList=lol_watcher.match.matchlist_by_puuid(data['puuid'])
        match = lol_watcher.match.by_id('euw1',matchList[0])
        for player in match['info']['participants']:
            if player['summonerName']=='Cinereos':
              champ = player["championName"]
              
               
              
        