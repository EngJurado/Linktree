from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/')
def index():
    name = 'Carlos Jurado'
    tags = 'Bioengineering | Brain modulation | Artificial Intelligence'
    description = "Passionate and dedicated professional with a strong foundation in bioengineering and artificial intelligence. Currently pursuing a Master's degree in AI to transition into a specialized AI career. Experienced in high-stress environments with a proven track record in problem-solving, teamwork, and leadership. Committed to continuous learning and development, holding multiple certifications in related technologies."
    links = [
        # Social and professional links to be included on the homepage
        {'name': 'GitHub', 'url': 'https://github.com/EngJurado', 'icon': 'fa-github'},
        {'name': 'LinkedIn', 'url': 'https://www.linkedin.com/in/engjurado/', 'icon': 'fa-linkedin'},
        {'name': 'Telegram', 'url': 'https://telegram.me/engjurado', 'icon': 'fa-telegram'},
        {'name': 'Twitter', 'url': 'https://twitter.com/EngJurado', 'icon': 'fa-x-twitter'}
    ]
    return render_template('index.html', name=name, tags=tags, description=description, links=links)  

if __name__ == '__main__':
    app.run()
