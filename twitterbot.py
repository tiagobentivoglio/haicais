# o robô que posta no tuíter a cada 15 minutos

def tuitar():

    while True:

        primeiro = gerador_verso(base)

        segundo = proximo_verso(primeiro)

        terceiro = proximo_verso(segundo)


        API_KEY = ''
        API_SECRET = ''
        ACCESS_TOKEN = ''
        ACCESS_SECRET = ''

        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

        api = tweepy.API(auth)

        # publicar tweet

        api.update_status(f'{primeiro}\n{segundo}\n{terceiro}')

        print('+1 tweet: ', '\n', f'{primeiro}\n{segundo}\n{terceiro}')

        # dar likes em resultados de pesquisa

        search = 'poesia'
        number = 5

        for tweet in tweepy.Cursor(api.search, search).items(number):
            tweet.favorite()

        pesquisa = 'sofrencia'
        number = 5

        for tweet in tweepy.Cursor(api.search, pesquisa).items(number):
            tweet.favorite()

        # esperar até a próxima postagem

        time.sleep(15*60)

tuitar()
