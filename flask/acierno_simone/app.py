from flask import Flask, render_template, request, redirect, url_for

#inizializza l'app Flask
app = Flask(__name__)
x="ciao"
lista=["a","b","c","d","e"]
#rotta principale

@app.route('/')
def home():
#render html e passiamo la lista
    return render_template('index.html', x=x, lista=lista)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    #ottiene elemento dal form
    elemento = request.form['elemento']
#aggiunge alla lista
    if elemento:
        lista.append(elemento)
        return redirect(url_for('home'))
    
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
    return redirect(url_for('home'))

@app.route('/clear', methods=['POST'])
def clear():
    lista.clear()
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)
    