from flask import Flask, render_template, url_for

# Initialize Flask application
app = Flask(__name__)

# Define route for the homepage
@app.route('/')
def index():
    # Personal and professional information to be displayed on the homepage
    name = 'Carlos Jurado'
    tags = 'Bioengineering | Brain modulation | Artificial Intelligence'
    description = "I am a dedicated professional with a comprehensive background in bioengineering and artificial intelligence. Currently, I serve as External Support at Medtronic, addressing complex challenges in high-stress environments. My career journey includes roles as a Laboratory Assistant and Research Student at the University of Antioquia. I am currently pursuing a Master's degree in Artificial Intelligence, eager to leverage my academic background in bioengineering and passion for AI technologies into a fulfilling career. Committed to continuous learning, I hold multiple certifications in related technologies, demonstrating my readiness to excel in the evolving landscape of AI."
    links = [
        # Social and professional links to be included on the homepage
        {'name': 'GitHub', 'url': 'https://github.com/EngJurado', 'icon': 'fa-github'},
        {'name': 'LinkedIn', 'url': 'https://www.linkedin.com/in/engjurado/', 'icon': 'fa-linkedin'},
        {'name': 'Telegram', 'url': 'https://telegram.me/engjurado', 'icon': 'fa-telegram'},
        {'name': 'Twitter', 'url': 'https://twitter.com/EngJurado', 'icon': 'fa-x-twitter'}
    ]
    # Render the homepage template with the provided information
    return render_template('index.html', name=name, tags=tags, description=description, links=links)

# Define route for handling 404 errors
@app.route("/<path:error404>")
def error404(error404):
    # Information to be displayed on the 404 error page
    name = 'Error 404'
    description = 'This page could not be found'
    # Render the 404 error template with the provided information
    return render_template('404.html', name=name, description=description)

# Run the Flask application if this script is executed as the main program
if __name__ == '__main__':
    app.run()
