from flask import Flask, render_template, redirect, request, url_for
import lyricsovh

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        song_name = request.form["song_name"]  
        artist_name = request.form["artist_name"]
        src = [song_name, artist_name]
        return redirect(url_for("output", song_name=song_name, artist_name=artist_name))
    else:  
        return render_template("index.html")

@app.route("/output/<song_name>/<artist_name>",)
def output(song_name, artist_name):
    return render_template("output.html", content=lyricsovh.lyrics(song_name, artist_name))

if __name__ == "__main__":
    app.run(debug=True)