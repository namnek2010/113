from flask import Flask, render_template
import json
import os

app = Flask(__name__)
counter_file = 'counter.json'

def read_counter():
    if not os.path.exists(counter_file):
        with open(counter_file, 'w') as f:
            json.dump({"visits": 0}, f)
    with open(counter_file, 'r') as f:
        data = json.load(f)
    return data["visits"]

def write_counter(count):
    with open(counter_file, 'w') as f:
        json.dump({"visits": count}, f)

@app.route('/')
def index():
    count = read_counter() + 1
    write_counter(count)
    return render_template('index.html', visits=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2580)
