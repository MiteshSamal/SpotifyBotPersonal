from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    # Placeholder playlist data (avoids needing Spotify API for tests)
    playlists = [
        {"name": "Chill Hits", "image": "", "tracks": 50},
        {"name": "Workout Mix", "image": "", "tracks": 30}
    ]
    return render_template("index.html", playlists=playlists)

@app.route("/volume", methods=["GET", "POST"])
def volume():
    volume_level = None

    if request.method == "POST":
        volume_level = request.form.get("volume")

    return render_template("volume.html", volume=volume_level)

if __name__ == "__main__":
    app.run(debug=True)