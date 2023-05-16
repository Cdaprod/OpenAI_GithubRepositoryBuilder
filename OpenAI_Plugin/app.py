import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/generate_project', methods=['POST'])
def generate_project():
    data = request.get_json()
    project_name = data['project_name']
    code = data['code']

    os.makedirs(f"Workspace/{project_name}", exist_ok=True)
    with open(f"Workspace/{project_name}/main.py", "w") as file:
        file.write(code)

    return {"status": "success"}, 200


if __name__ == '__main__':
    app.run(debug=True)
