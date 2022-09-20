from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def home():
    return """<html>
                <body>
                    <h1>Activity 3</h1>
                    <form action="/NameChar">
                        <h2>What's your name?</h2><h4> <input type='text' name='name'></h4>
                        <h2>What's your characteristic?</h2><h4> <input type='text' name='char'><h4>
                        <input type='submit' value='SUBMIT'>
                    </form>    
                </body>
                </html>"""

@app.route('/NameChar')
def NameChar():
    name = request.args.get('name')
    if name == '':
        name = 'Name: <u>You did not put your Name!</u>'
    else:
        name = 'My Name is'' <u>'+name+'</u>'

    char = request.args['char'] 
    if char == '':
        msg = 'Characteristic: <u>You did not put your Characteristic!</u>'
    else:
        msg =  'My Characteristic is'' <u>'+char+'.</u>'
    return """
            <html>
                <body>
                    <h1>Activity 3</h1>
                    <h4> {0}</h4>
                    <h4> {1}</h4>
            <form action="/">
                <input type='submit' value='BACK'>
            </form>
                </body>
            </html>
            """.format(name,msg)

app.run(host="localhost", debug=True)