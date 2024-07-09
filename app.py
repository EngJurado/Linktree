from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Carlos Jurado'
    tags = 'Bioengineering | Brain modulation | Artificial Intelligence'
    description = "Bioengineer with a passion for neuromodulation, machine learning, and data analysis. Currently pursuing a Master's degree in Artificial Intelligence. Experienced in providing clinical support for neuromodulation surgeries and programming neurostimulators. Skilled in patient education, surgical support, medical devices, and leadership."
    links = [
        {
            'name': 'GitHub',
            'url': 'https://github.com/EngJurado',
            'icon': 'fa-github'
        },
        {
            'name': 'LinkedIn',
            'url': 'https://www.linkedin.com/in/engjurado/',
            'icon': 'fa-linkedin'
        },
        {
            'name': 'Telegram',
            'url': 'https://telegram.me/engjurado',
            'icon': 'fa-telegram'
        },
        {
            'name': 'Twitter',
            'url': 'https://twitter.com/EngJurado',
            'icon': 'fa-twitter'
        }
    ]
    return render_template('index.html', name = name, tags = tags, description = description, links = links)

@app.route("/<path:error404>")
def error404(error404):
    name = 'Error 404'
    description = 'This page could not be found'
    return render_template('404.html', name = name, description = description)

if __name__ == '__main__':
    app.run()
