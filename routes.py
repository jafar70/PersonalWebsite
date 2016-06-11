from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
import os

mail = Mail()

app = Flask(__name__)
app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'jsalami60@gmail.com'
app.config["MAIL_PASSWORD"] = 'osalami20'

mail.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")
    
@app.route("/cusu")
def cusu():
    return render_template("cusu.html")
    
@app.route("/fdm")
def fdm():
    return render_template("fdm.html")
    
@app.route("/jcci")
def jcci():
    return render_template("jcci.html")

@app.route("/kobe")
def kobe():
    return render_template("kobe.html")
    
@app.route("/oddfuture")
def oddfuture():
    return render_template("oddfuture.html")
    
@app.route("/westfield")
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
