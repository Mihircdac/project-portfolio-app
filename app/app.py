from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample project data
PROJECTS = {
    "user1": [
        {"name": "Project A", "description": "Description for project A", "link": "/user1/project-a"},
        {"name": "Project B", "description": "Description for project B", "link": "/user1/project-b"}
    ],
    "user2": [
        {"name": "Project X", "description": "Description for project X", "link": "/user2/project-x"},
        {"name": "Project Y", "description": "Description for project Y", "link": "/user2/project-y"}
    ],
}

@app.route("/")
def homepage():
    return render_template("index.html", projects=PROJECTS)

@app.route("/<user>")
def user_projects(user):
    return jsonify(PROJECTS.get(user, []))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
