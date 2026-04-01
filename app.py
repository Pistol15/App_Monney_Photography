from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title="home")

@app.route('/menu')
def menu():
    return render_template('menu.html', title="menu")

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio/portfolio.html', title="portfolio")

if __name__ == '__main__':
    # Mode debug activé pour le développement
    app.run(debug=True)