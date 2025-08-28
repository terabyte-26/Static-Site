from flask import Flask, render_template, send_from_directory, abort

# Disable Flask's default /static so we can expose /comp and /assets exactly as requested
app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config["TEMPLATES_AUTO_RELOAD"] = True


# -------------------------
# Page routes
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")


# -------------------------
# Static file serving
# -------------------------
# Serve files under /comp/... (CSS/JS)
@app.route("/comp/<path:filename>", strict_slashes=False)
def comp_file(filename):
    return send_from_directory("comp", filename)

# Serve files under /assets/... (images and other assets)
@app.route("/assets/<path:filename>", strict_slashes=False)
def assets_file(filename):
    return send_from_directory("assets", filename)



# Nice-to-have: favicon/robots fallback (avoid noisy 404s)
@app.route("/favicon.ico")
def favicon():
    try:
        return send_from_directory("assets", "images/favicon.ico")
    except Exception:
        abort(404)

@app.route("/robots.txt")
def robots():
    try:
        return send_from_directory(".", "robots.txt")
    except Exception:
        abort(404)


if __name__ == "__main__":
    # Run locally: python main.py
    app.run(host="0.0.0.0", port=5000, debug=True)
