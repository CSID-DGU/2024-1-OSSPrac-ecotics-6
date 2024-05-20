from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method =='POST':
       result=dict()
       result['Name']=request.form.get('Name')
       result['StudentNumber']=request.form.get('StudentNumber')
       result['University']=request.form.get('University')
       result['Major']=request.form.get('Major') 
       result['Gender']=request.form.get('Gender')
       result['Email']=request.form.get('Email')
       result['language']=request.form.getlist('language')
       return render_template('result.html',result=result)

if __name__ =='__main__':
     app.run(debug=True)