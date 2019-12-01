class Web:

	def web_page():
		if drain.value() == 1:
		  gpio_state="ON"
		else:
		  gpio_state="OFF"
		  
		html = """<html>
		<head>
		<title>ESP Web Server</title>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="icon" href="data:,"> 
		<style>
		html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
		h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}
		.button{display: inline-block; background-color: #e7bd3b; border: none; 
		border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
		.button2{background-color: #4286f4;}
		</style>
		</head>
		<body> 
		<h1>Keg Cleaner Web Server</h1> 
		<p>GPIO state: <strong>""" + gpio_state + """</strong></p>
		<p>
		<a href="/?start=on">
		<button class="button">START</button>
		</a>
		</p>
		<p>
		<a href="/?start=off"><button class="button button2">STOP</button></a>
		</p>
		</body>
		</html>"""
		return html



  