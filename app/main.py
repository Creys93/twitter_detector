import tweepy
from flask import Flask, request, jsonify

# Configuración de las claves de la API de Twitter (obtén tus propias claves en https://developer.twitter.com/)
consumer_key = 'TU_CONSUMER_KEY'
consumer_secret = 'TU_CONSUMER_SECRET'
access_token = 'TU_ACCESS_TOKEN'
access_token_secret = 'TU_ACCESS_TOKEN_SECRET'

# Configuración de autenticación de Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Crear una instancia de la API de Twitter
api = tweepy.API(auth)

# Configuración de Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    try:
        return 'Hola'
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/', methods=['POST'])
def webhook():
    try:
        data = request.json
        tweet_text = data['text']
        user_name = data['user']['screen_name']
        
        # Aquí puedes agregar tu lógica para procesar el tweet
        # Por ejemplo, verificar si es un comentario falso y tomar medidas
        
        # En este ejemplo, simplemente imprimiremos el tweet recibido
        print(f"Tweet de @{user_name}: {tweet_text}")
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
