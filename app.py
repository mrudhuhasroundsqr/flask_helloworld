from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['Debug'] = True


@app.route('/helloworld', methods=['GET', 'POST'])
def getAnn():
    if request.method == 'POST':
        return jsonify({"success": "Hello world"})
    else:
        return jsonify({"success": "method not allowed"})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
