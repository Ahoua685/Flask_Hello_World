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

@app.route('/')
def index(): 
        valeurs = request.args.get('valeurs', '')
        valeurs_entiers = [int(valeur) for valeur in valeurs.split(',') if valeur.strip().isdigit()]
        somme = sum(valeurs_entiers)
        valeur_max = max(valeurs_entiers)if valeurs_entiers else None
        parite = "pair" if somme % 2 == 0 else "impair" 
    reponse = f"<h2>La somme de vos valeurs est: {somme} et elle est {parite}.</h2>"
    if valeur_max is not None:
        reponse += f"<h3>La valeur maximale saisie est: {valeur_max}.</h3>"
    else:
        reponse += "<h3>Aucune valeur valide saisie.</h3>"
    return reponse         

if __name__ == "__main__":
  app.run(debug=True)
