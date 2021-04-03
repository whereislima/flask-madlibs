from flask import Flask, request, render_template

from flask_debugtoolbar import DebugToolbarExtension

from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "mangoes"

debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    """ Return Homepage """
    #
    # didnt know i could access prompts from the init method? 
    prompts = story.prompts
    return render_template("madlibs.html", prompts=prompts)


@app.route('/story')
def show_story():
    """ Return your story """
    # place = request.args["place"]
    # noun = request.args["noun"]
    # verb = request.args["verb"]
    # adjective = request.args["adjective"]
    # plural_noun = request.args["plural-noun"]

    # return render_template("story.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)

    text = story.generate(request.args)

    return render_template("story.html", text=text)    