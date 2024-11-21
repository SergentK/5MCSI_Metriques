from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') 

@app.route("/contact/")
def Moncontact():
    return render_template("contact.html")

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route('/histogramme/')
def histogramme():
    return render_template('histogramme.html')

import requests
from datetime import datetime

@app.route("/commits/")
def commits():
    import requests
    from flask import jsonify
    from datetime import datetime

    try:
        # Récupérer les données depuis l'API GitHub
        url = "https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits"
        response = requests.get(url, timeout=10)
        commits_data = response.json()

        # Compter les commits par heure
        commits_count = {}
        for commit in commits_data:
            date_string = commit["commit"]["author"]["date"]
            date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
            minute = date_object.strftime('%H:%M')
            commits_count[minute] = commits_count.get(minute, 0) + 1

        # Retourner les résultats en JSON
        return jsonify(commits_count)

    except Exception as e:
        return jsonify({"error": str(e)})




if __name__ == "__main__":
    app.run(debug=True)
  
if __name__ == "__main__":
  app.run(debug=True)
