from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Lade die WADA-Daten aus der JSON-Datei
with open("wada_data.json", "r") as f:
    wada_list = json.load(f)

# Endpunkt zum Abgleich der Substanz
@app.route('/check-substance', methods=['POST'])
def check_substance():
    data = request.json
    substance = data.get("substance", "").lower()
    
    # Prüfen, ob Substanz in der WADA-Liste enthalten ist
    forbidden = any(substance in item["substance"].lower() for item in wada_list)
    if forbidden:
        return jsonify({"result": "forbidden", "message": "Die Substanz ist verboten!"})
    return jsonify({"result": "allowed", "message": "Die Substanz ist erlaubt!"})

if __name__ == '__main__':
    app.run(debug=True)
