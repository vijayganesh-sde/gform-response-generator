from flask import Flask, render_template, request
from app import generate_responses
app=Flask(__name__)
form_link = None
@app.route("/",methods=["GET", "POST"])
def index():
  return render_template('index.html')
@app.route("/generate_responses",methods=["GET","POST"])
def generate():
  if request.method == "POST":
    no_of_resp=int(request.form['resp'])
    form_link=request.form['link']
  try:
    generate_responses(no_of_resp,form_link)
    return "SUCCESS"
  except:
    return "ERROR"
PORT=5000
app.run(debug=True)