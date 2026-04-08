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

@app.route('/MotocrossBroc2025')
def MotocrossBroc2025():
    return render_template('portfolio/Motocross_de_Broc_2025.html', title="Motocross de Broc 2025")

@app.route('/MotocrossTrey2025')
def MotocrossTrey2025():
    return render_template('portfolio/Motocross_de_Trey_2025.html', title="Motocros de Trey 2025")

@app.route('/MotocrossCournillens2025')
def MotocrossCournillens2025():
    return render_template('portfolio/Motocross_de_Cournillens_2025.html', title="Motocros de Cournillens 2025")

@app.route('/MotocrossSergey2025')
def MotocrossSergey2025():
    return render_template('portfolio/Motocross_de_Sergey_2025.html', title="Motocros de Sergey 2025")

if __name__ == '__main__':
    # Mode debug activé pour le développement
    app.run(debug=True)