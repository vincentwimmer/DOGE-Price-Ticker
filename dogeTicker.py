from websocket import create_connection
import json
import time

# Header
headers = json.dumps({
	"Accept-Encoding" : "gzip, deflate, br",
	"Accept-Language" : "en-US,en;q=0.9",
	"Cache-Control" : "no-cache",
	"Connection" : "Upgrade",
	"Host" : "stream.coinmarketcap.com",
	"Origin" : "https://coinmarketcap.com",
	"Pragma" : "no-cache",
	"Sec-WebSocket-Extensions" : "permessage-deflate; client_max_window_bits",
	"Sec-WebSocket-Key" : "YEExioPDcVAWNmM1N1lD4g==",
	"Sec-WebSocket-Version" : "13",
	"Upgrade" : "websocket",
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
})

# Create Connection
ws = create_connection('wss://stream.coinmarketcap.com/price/latest',headers=headers)

# Handshake
ws.send('{"method":"subscribe","id":"price","data":{"cryptoIds":[74],"index":"detail"}}')

# Print Received Info
while True:
	try:
		result = ws.recv()
		try: 
			b = json.loads(result)
			print(b['d']['cr']['p'])
		except:
			print(result)

		time.sleep(5)

	except Exception as e:
		print(e)
		break
