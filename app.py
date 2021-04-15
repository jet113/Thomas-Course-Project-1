from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
import docker
import sys
import subprocess
app = Flask(__name__)


@app.route("/")
def hello():
	client = docker.from_env()
	for container in client.containers.list():
		print(container.name, file=sys.stderr)
		print(container, file=sys.stderr)
	return render_template("main.html")

@app.route("/tf")
def tf():
	client = docker.from_env()
	for container in client.containers.list():
		if container.name == 'tensorflow':
			container.exec_run("xterm")
	return redirect(url_for('hello'))

@app.route("/git")
def git():
	client = docker.from_env()
	for container in client.containers.list():
		if container.name == 'git':
			container.exec_run("xterm")
	return redirect(url_for('hello'))

@app.route("/hadoop")
def hadoop():
	client = docker.from_env()
	for container in client.containers.list():
		if container.name == 'hadoop':
			container.exec_run("xterm")
	return redirect(url_for('hello'))

@app.route("/pyspark")
def pyspark():
	client = docker.from_env()
	for container in client.containers.list():
		if container.name == 'pyspark':
			container.exec_run("xterm")
	return redirect(url_for('hello'))

@app.route("/spyder")
def spyder():
	client = docker.from_env()
	for container in client.containers.list():
		if container.name == 'spyder':
			container.exec_run("spyder3")
	return redirect(url_for('hello'))

@app.route("/orange")
def orange():
	client = docker.from_env()
	for container in client.containers.list():
		if container.name == 'orange':
			container.exec_run("source orange3venv/bin/activate")
			container.exec_run("orange-canvas")
	return redirect(url_for('hello'))