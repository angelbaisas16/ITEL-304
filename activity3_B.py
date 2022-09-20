from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def home():
    return """<html>
                <body>
                
                    <h1>Activity 3.B</h1>
                   <form action="/PerInfo">
                        <h2>FILL-UP YOUR INFORMATION BELOW:</h2>
                        

                        <h4>First Name: <input type='text' name='fname'> Last Name: <input type='text' name='lname'> MI: <input type='text' name='midin'></h4>
                        <h4> Age: <input type='text' name='age'><h4>
                        <h4> Date of Birth: <input type='text' name='dob'><h4>
                        <h4> Place of Birth: <input type='text' name='pob'><h4>
                        <h4> Civil Status: <input type='text' name='civils'><h4>
                        <h4> Height: <input type='text' name='height'><h4>
                        <h4> Nationality: <input type='text' name='nationality'><h4>
                        <h4> Religion: <input type='text' name='religion'><h4>
                        <h4> Language: <input type='text' name='language'><h4>
                        <h4> Father's name: <input type='text' name='fathern'><h4>
                        <h4> Mother's name: <input type='text' name='mothern'><h4>
                        <input type='submit' value='SUBMIT'>
                    </form> 
                       
                </body>
                </html>"""

@app.route('/PerInfo')
def PerInfo():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    midin = request.args.get('midin')
    age = request.args.get('age')
    dob = request.args.get('dob')
    pob = request.args.get('pob')
    civils = request.args.get('civils')
    height = request.args.get('height')
    nationality = request.args.get('nationality')
    religion = request.args.get('religion')
    language = request.args.get('language')
    fathern = request.args.get('fathern')
    mothern = request.args.get('mothern')
    
   

    if fname == '':
        fname = 'Firstname: <u>______N/A______</u>'
    else:
        fname = 'Firstname:  ''<u>_____'+fname+'_____</u>'
    if lname == '':
        lname = 'Lastname: <u>______N/A______</u>'
    else:
        lname = 'Lastname:  ''<u>_____'+lname+'_____</u>'
    if midin == '':
        midin = 'MI: <u>______N/A______</u>'
    else:
        midin = 'MI:  ''<u>_____'+midin+'_____</u>'
    if age == '':
        age = 'Age: <u>______N/A______</u>'
    else:
        age = 'Age: ''<u>_____'+age+'_____</u>'
    if dob == '':
        dob = 'Date of Birth: <u>______N/A______</u>'
    else:
        dob = 'Date of Birth: ''<u>_____'+dob+'_____</u>'
    if pob == '':
        pob = 'Place of Birth: <u>______N/A______</u>'
    else:
        pob = 'Place of Birth: ''<u>_____'+pob+'_____</u>'
    if civils == '':
        civils = 'Civil Status: <u>______N/A______</u>'
    else:
        civils = 'Civil Status: ''<u>_____'+civils+'_____</u>'
    if height == '':
        height = 'Height: <u>______N/A______</u>'
    else:
        height = 'Height: ''<u>_____'+height+'_____</u>'
    if nationality == '':
        nationality = 'Nationality: <u>______N/A______</u>'
    else:
        nationality = 'Nationality: ''<u>_____'+nationality+'_____</u>'
    if religion == '':
        religion = 'Religion: <u>______N/A______</u>'
    else:
        religion = 'Religion: ''<u>_____'+religion+'_____</u>'
    if language == '':
        language = 'Language: <u>______N/A______</u>'
    else:
        language = 'Language: ''<u>_____'+language+'_____</u>'
    if fathern == '':
        fathern = 'Fathers name: <u>______N/A______</u>'
    else:
        fathern = 'Fathers name: ''<u>_____'+fathern+'_____</u>'
    if mothern == '':
        mothern = 'Mothers name: <u>______N/A______</u>'
    else:
        mothern = 'Mothers name: ''<u>_____'+mothern+'_____</u>'
    
    return """
            <html>
                <body>
                    <h1>PERSONAL <br>INFORMATION</h1>
                    <h4> {0} </h4>
                    <h4> {2} {1}</h4>
                    <h4> {3}</h4>
                    <h4> {4}</h4>
                    <h4> {5}</h4>
                    <h4> {6}</h4>
                    <h4> {7}</h4>
                    <h4> {8}</h4>
                    <h4> {9}</h4>
                    <h4> {10}</h4>
                    <h4> {11}</h4>
                    <h4> {12}</h4>
                    
            <form action="/">
                <input type='submit' value='BACK'>
            </form>
                </body>
            </html>
            """.format(fname,lname,midin,age,dob,pob,civils,height,nationality,religion,language,fathern,mothern)

app.run(host="localhost", debug=True)