import tweepy 
import time
import random

auth = tweepy.OAuthHandler('7docZNy3gfhJZKeQJWYvKK1x2', '3tTcpkhR23oefPiqqJ13OT1OAULlNfgVVvgrR32xiXUnV1eEBR')
auth.set_access_token('1300088460619984897-I05axT8KWk9SWOFbW6kREgvEhEQnil', 'gaIZVjAod2lUUbS5Gre5SyLaLVDAVDJVHy0nBNamZeE7Y')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

print(user.name)

hashtags = ['#bolsonaro2022', '#FechadoComBolsonaro', '#ToComDamares', '#20MesesSemCorrupcao', '#FechadoComBolsonaroAte2026', '#600DiasdeGoverno', '#Bolsonaro2022', '#SomosTodosRicardoSalles', 'Bolsonaro até morrer', '#FechadoComBolsonaro', '#GloboLixo', '#globolixo', '#GLOBOLIXO', 'Bolsonaro parabéns', '#ForaMaia', '#ForaAlcolmbre', '#prasemprebolsonaro', '#GloboInimigaDoBrasil', '#globoinimigadoBrasil', '#GloboNão', '#SouBolsonaroAteMorrer', '#SouBolsonaro', '#MoroLadrão', '#MoroTraidor']

def hashtagsRandom():
    hashtagsLength = len(hashtags)
    return random.randint(0, hashtagsLength - 1)

while True:
    rand = hashtagsRandom()
    for tweet in tweepy.Cursor(api.search, hashtags[rand]).items(1):
        try:
            print('[SUCESS] - Retweet done!' + ' - Keyword: ' + hashtags[rand])
            tweet.retweet()
            time.sleep(60*30)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    
