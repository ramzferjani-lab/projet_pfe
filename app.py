from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"
# DEPARTEMENTS

@app.route('/cms_manuel')
def cms_manuel():
    return render_template("cms_manuel.html")
@app.route('/magasin')
def magasin():
    return render_template("magasin.html")



@app.route('/cms_robotise')
def cms_robotise():
    return render_template("cms_robotise.html")


@app.route('/controle_test')
def controle_test():
    return render_template("controle_test.html")


@app.route('/emballage')
def emballage():
    return render_template("emballage.html")


# comptes autorisés
users = {
    "setti sofien": "la pratique2001",
    "admin": "admin"
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:

            session['user'] = username
            return redirect(url_for('dashboard'))

        else:
            return render_template("login.html", error="Login incorrect")

    return render_template("login.html")


@app.route('/dashboard')
def dashboard():

    if 'user' in session:
        return render_template("dashboard.html")

    return redirect(url_for('login'))


@app.route('/cmsmanuel')
def cmsmanuel():

    if 'user' in session:
        return render_template("cms_manuel.html")

    return redirect(url_for('login'))


@app.route('/logout')
def logout():

    session.pop('user',None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
