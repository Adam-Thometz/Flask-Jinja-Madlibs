from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'what_would_jeff_do'
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('home.html', prompts = story.prompts)

@app.route('/story')
def show_madlib():
    
    text = story.generate(request.args)

    return render_template('story.html', text = text)