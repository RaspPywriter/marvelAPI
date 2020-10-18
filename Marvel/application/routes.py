from flask import Flask, request, render_template
from application import app, db, editing as ed
import json
from application.model import Comic


# page to go home
@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('home.html')


# page that goes to type
@app.route("/characters")
def characters():
    return render_template("characters.html")


@app.route("/comics", methods=['GET', 'POST'])
def comics():
    if request == 'POST':
        data = json.loads(request.data)
    return render_template("comics.html")

@app.route('/game', methods=['POST' ,'GET'])
def game():

    names= []
    for desc in Comic.objects:
        if Comic.description != "":
            names.append(desc.name)

    return render_template('game.html', nameOnly=names)

@app.route('/SaveFile', methods=['POST', 'GET'])
def SaveFile():

    if request.method == "POST":
        # converts to a python object - in this case dictionary
        data = request.get_json()
        # as you go along - save it in a variable so it's easier to analyze
        d = data['data']
        results = d['results']
        # when you pull the results, they are in a list but results[0] returns each hero
        for i in results:
            '''
            iterating through results returns a dictionary for each character so for name and description you can just
            pull the key and get the value, for the other 3 it is more work
            '''
            name = i['name']
            description = i['description']
            comics = i['comics']
            s = i['stories']
            e = i['events']
            se = i['series']
            # comics, stories, events are each nested dictionaries so they need to be further processed
            c = comics['items']
            # c is a list with a dictionary inside so do the following to get at those values same for event and stories
            comicStrip = []
            for d in c:
                comicStrip.append(d['name'])
            st = s['items']
            stories = []
            for ea in st:
                stories.append(ea['name'])
            ev = e['items']
            events = []
            for event in ev:
                events.append(event['name'])
            print(events)
            ser = se['items']
            series = []
            for serie in ser:
                series.append(serie['name'])

            comic= Comic(name=name, description=description,comicStrip=comicStrip,stories=stories,events=events,series=series)
            comic.save()

        return render_template('comics.html')
