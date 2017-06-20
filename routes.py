from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail
import os

mail = Mail()

app = Flask(__name__)
app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.mail.com"
app.config["MAIL_PORT"] = 993
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'jafarocean@mail.com'
app.config["MAIL_PASSWORD"] = 'Osalami20_'

mail.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")
    
@app.route("/portfolio/cusu")
def cusu():
    return render_template("cusu.html")
    
@app.route("/portfolio/fdm")
def fdm():
    return render_template("fdm.html")
    
@app.route("/portfolio/studentsupport")
def studentsupport():
    return render_template("studentsupport.html")
    
@app.route("/portfolio/mannssolutions")
def mannssolutions():
    return render_template("mannssolutions.html")    

@app.route("/portfolio/niyati")
def niyati():
    return render_template("niyati.html")

@app.route("/portfolio/cloud9")
def cloud9():
    return render_template("c9.html")
    
@app.route("/portfolio/webapi")
def webapi():
    return render_template("webapi.html")
    
@app.route("/portfolio/starfighter")
def starfighter():
    return render_template("starfighter.html")
    
@app.route("/portfolio/qube")
def qube():
    return render_template("qube.html")

@app.route("/portfolio/aaronclarey")
def aaronclarey():
    return render_template("aaronclarey.html")
    
@app.route("/portfolio/visdata")
def visdata():
    return render_template("visdata.html")
    
@app.route("/portfolio/westfield")
def westfield():
    return render_template("westfield.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)
