#building URL Dynamically
## Variable Rule
# Jinja 2 Template Engine

## jinja 2 Template Engine 
'''
    there are multiple ways to output the html 
    1: {{}} simple output
    2: {%.....%} conditions, for loops
    3: {#.....#} Comments
'''


from flask import Flask, render_template,request,redirect,url_for


app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method=='POST':
            name = request.form['name']
            return f"Hello {name}!, You have submitted the form thank you"
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res="pass"
    else:
        res="fail"
    
    return render_template('result.html', result=res) 

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res="pass"
    else:
        res="fail"
    
    exp = {'result': res, 'score':score}
    
    return render_template('index1.html', expression=exp) 

@app.route('/successif/<int:score>')
def successrif(score):
    return render_template('result.html', result=score) 


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', result=score) 


@app.route('/getresult', methods=['GET', 'POST'])
def getResult():
    if request.method == 'POST':
        chem = int(request.form['chem'])
        c = int(request.form['c'])
        marks = [chem, c]
        avg = sum(marks) / len(marks)
    else:
        return render_template('getResult.html')
        
    return redirect(url_for('successres' , score=avg))
                       
if __name__=='__main__':
    app.run(debug=True)
    
