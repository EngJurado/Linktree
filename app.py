from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Carlos Jurado'
    tags = 'Bioengineering | Brain modulation | Artificial Intelligence'
    description = "I am a dedicated professional with a comprehensive background in bioengineering and artificial intelligence. Currently, I serve as a Clinical Specialist at Medtronic, where I utilize my expertise to address complex challenges in high-stress environments. My career journey has been enriched by various roles, including those of Laboratory Assistant and Research Student at the University of Antioquia."
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
