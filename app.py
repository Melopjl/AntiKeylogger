from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from config import Config
from services.scan_service import ScanService
from scanner.monitor import Monitor

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = "supersecretkey"

# Inicializa o serviço de scan e monitor
scanner = ScanService()
monitor = Monitor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/scan", methods=["POST"])
def scan():
    result = scanner.run_scan()
    flash(result, "info")
    return redirect(url_for("dashboard"))

@app.route("/logs")
def logs():
    try:
        with open(Config.LOG_PATH, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        return jsonify({"logs": content})
    except Exception as e:
        return jsonify({"logs": f"Erro ao carregar logs: {e}"})

@app.route("/processes")
def processes():
    procs = monitor.list_processes()
    return jsonify({"processes": procs})

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
