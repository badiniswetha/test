
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 17:57:51 2020

@author: sowmy
"""


from flask import Flask , render_template , request
app = Flask(__name__) # interfacee between by server and my application wsgi
import pickle
model=pickle.load(open('energy1.pkl','rb'))

@app.route('/') # bind to an url 
def helloworld():
    return render_template("index1.html")
@app.route('/login',methods = ['POST']) # bind to an url 
def admin():
    p = request.form["ws"]
    q = request.form["tpc"]
    r = request.form["wd"]
    w = request.form["w"]
    if(w=="Cloudy"):
        w1,w2,w3,w4=1,0,0,0
    if(w=="Rainy"):
        w1,w2,w3,w4=0,1,0,0
    if(w=="Sunny"):
        w1,w2,w3,w4=0,0,1,0
    if(w=="Windy"):
        w1,w2,w3,w4=0,0,0,1
    t = [[int(w1),int(w2),int(w3),int(w4),int(p),int(q),int(r)]]
    y = model.predict(t)
    return render_template("index1.html", y="The predicted energy would be:" +str(y[0]))

@app.route('/user')#url
def user():
    return "hie user"

if __name__ == '__main__' :
    app.run(debug =True)
