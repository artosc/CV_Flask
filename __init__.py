from flask import Flask, render_template_string, render_template, jsonify
from flask import Flask, render_template, request, redirect
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("resume_1.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    try:
        if request.method == 'POST':
            # Récupérer les données du formulaire
            email = request.form['email']
            message = request.form['message']

            # Insérer les données dans la base de données
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO messages (email, message) VALUES (?, ?)', (email, message))
                conn.commit()

            # Rediriger vers la page de consultation des messages après l'ajout
            return redirect(url_for('ReadBDD'))

        # Si la méthode est GET, simplement rendre le template du formulaire
        return render_template('messages.html')

    except Exception as e:
        print("Une erreur s'est produite : ", str(e))
        print(traceback.format_exc())
        return str(e), 500

# Création d'une nouvelle route pour la lecture de la BDD
@app.route("/consultation/")
def ReadBDD():
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM messages_cv WHERE id = ?', (post_id,)).fetchone()
    conn.close()

    # Si la publication avec l'ID spécifié n'est pas trouvée, renvoie une réponse 404 Not Found
    if post is None:
        return jsonify(error='Post not found'), 404

    # Convertit la publication en un format JSON
    json_post = {'id': post['id'], 'email': post['email'], 'message': post['message']}
    
    # Renvoie la réponse JSON
    return jsonify(post=json_post)

if(__name__ == "__main__"):
    app.run()





                                                                                                                                                                                                                  
import sqlite3
                                                                                                                                                                                                                   
connection = sqlite3.connect('database.db')
                                                                                                                                                                                                                   
with open('schema.sql') as f:
    connection.executescript(f.read())                                                                                                                                                                             
                                                                                                                                                                                                                   
cur = connection.cursor()                                                                                                                                                                                          
insert = "INSERT INTO messages_cv (email, message) VALUES (?, ?)",                                                                                                                                                                                                                   
                                                                                                                                                            
connection.close()                                                                                                                                                                                                 
                                  