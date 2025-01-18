from flask import Flask, jsonify, request, make_response
import json
app = Flask(__name__)

data_file_path = "./films.json"

# Route pour renvoyer des données JSON
@app.route('/')
def home():
    return jsonify({
        'message': 'Hello depuis l\'API',
        'status': 'success'
    })

def read_file():
    with open(data_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def save_file(data):
    with open(data_file_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4))

@app.route('/movies')
def get_movies():
    err=""
    try:
        data = read_file()
        
        if "films" in data:
            data["status"]='success'

            return jsonify(data)
        else:
            err=" `films` not found in the data base "
    except Exception as e:
        err=str(e)
    return jsonify({
        'error': f'Internal server Error: `{err}`',
        'status': 'error'
    })

@app.route('/add_movie', methods=['POST'])
def add_movie():
    try:
        movie = request.get_json()
        if isinstance(movie, dict) and "title" in movie and isinstance(movie["title"], str) \
        and "genre" in movie and isinstance(movie["genre"], list) \
        and "description" in movie and isinstance(movie["description"], str):
            data = read_file()
            data["films"].append(movie)
            save_file(data)
            return "success", 200
        else:
            return "format error", 500
    except Exception as e:
        return f"Internal server error : `{e}`", 500


@app.route('/del_movie', methods=['POST'])
def del_movie():
    try:
        movie = request.get_json()
        if isinstance(movie, dict) and "title" in movie and isinstance(movie["title"], str):
            title = movie["title"]
            data = []
            for d in read_file()["films"]:
                if title != d['title']:
                    data.append(d)
            save_file({"films":data})
            return "success", 200
        else:
            return "format error", 500
    except Exception as e:
        print(f"Internal server error : `{e}`")
        return f"Internal server error : `{e}`", 500



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Exposé sur le port 5000
