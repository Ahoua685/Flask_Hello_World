from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html') #comm2

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html") 

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

#@app.route('/somme/<int:valeur1>/<int:valeur2>')
#def somme(valeur1,valeur2):
#    result= valeur1 + valeur2
#    return f"<h2>La somme de votre valeur est:  </h2> {result}"
@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    result = valeur1 + valeur2
    if result % 2 == 0:
        parite = "pair"
    else:
        parite = "impair" 
    return f"<h2>La somme de vos valeurs est: {result} et elle est {parite}.</h2>"

@app.route('/somme_toutes/<values>')
def somme_toutes(values): 
    valeurs = map(int, values.split(','))
    resultat = sum(valeurs)  
    return f"<h2>La somme de toutes les valeurs est: {resultat} </h2>" 

@app.route('/valeur_max/<values>')
def valeur_max(values):
    valeurs = map(int, values.split(','))
    max_valeur = max(valeurs)
    return f"<h2>La valeur maximale est: {max_valeur} </h2>"
    
@app.route('/cv')
def cv():
    return render_template('cv.html') #comm2
    
@app.route('/page1')
def page1():
    return render_template('page1.html') #comm2
@app.route('/actualite')
def actualite():
    return render_template('actualite.html') #comm2
@app.route('/outilsJS')
def outilsJS():
    return render_template('outilsJS.html') #comm2        
@app.route('/bibloimages')
def bibloimages():
    return render_template('bibloimages.html') 
@app.route('/Carre_Etoile') 
def carre_etoiles():
    return render_template('Carre_Etoiles.html')   

if __name__ == "__main__":
  app.run(debug=True)
