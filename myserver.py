from flask import Flask

app = Flask("demoServer")

@app.route('/')
def helloIndex():
    return 'Hello World from Python Flask!'

app.run(host='0.0.0.0', port=80)