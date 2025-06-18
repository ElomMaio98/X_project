import tweepy 
import os
from dotenv import load_dotenv

load_dotenv()
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

def autenticar_api():
    print('Tentando autenticar...')
    try: 
        auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        api= tweepy.API(auth)
        api.verify_credentials()
        print("Autenticação bem sucedida")
        return api
    except tweepy.TweepyException as e:
        print(f"Erro ao autenticar na API: {e}, verificar credenciais")
        return None

def obter_informacoes_usuario(api,username):
    if not api:
        print("Não houve autenticação da API, não é possível buscar dados")
        return
    print(f"\nBuscando informações para o usuário: @{username}...")
    
    try:
        user = api.get_user(screen_name=username)
        print("\n--- Informações do Usuário ---")
        print(f"Nome: {user.name}")
        print(f"Nome de Usuário (Handle): @{user.screen_name}")
        print(f"ID do Usuário: {user.id}")
        print(f"Descrição: {user.description}")
        print(f"Localização: {user.location}")
        print(f"URL do Perfil: https://twitter.com/{user.screen_name}")
        print(f"Número de Seguidores: {user.followers_count}")
        print(f"Número de Seguindo: {user.friends_count}")
        print(f"Número de Tweets: {user.statuses_count}")
        print(f"Verificado: {'Sim' if user.verified else 'Não'}")
        print(f"Criado em: {user.created_at}")
        print("----------------------------")
    except tweepy.TweepyException as e:
        print(f"Erro ao obter informações do usuário '{username}': {e}")
        print("Certifique-se de que o nome de usuário está correto e existe.")

if __name__ == "__main__":
    api_autenticada = autenticar_api()
    if api_autenticada:
        usuario_alvo = input("\nDigite o nome de usuário do Twitter: ")
        obter_informacoes_usuario(api_autenticada, usuario_alvo)
