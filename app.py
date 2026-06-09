from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="ar">
    <head>
        <meta charset="UTF-8">
        <title>3CX Webclient - بيئة اختبارية</title>
    </head>
    <body>
        <h1>Welcome to 3CX Webclient Testing Server</h1>
        <p>This is a local simulated laboratory environment.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
