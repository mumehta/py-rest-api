from flask import render_template # Remove: import Flask
import connexion
import people

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/")
def home():
    peoples = people.show_people()
    return render_template("home.html", people=peoples)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)