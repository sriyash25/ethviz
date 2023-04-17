from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/dynamic_node_generation', methods=['POST'])
def dynamic_node_generation():

    # execute the Python script
    current_dir = os.getcwd()
    mydir = f'{current_dir}/src/salian_script.py'
    print(mydir)
    subprocess.run(['python3', mydir])

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
