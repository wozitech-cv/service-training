from flask import (
  Flask,
  render_template
)
app = Flask(__name__, template_folder='templates')

@app.route('/')
def training():
  return render_template('home.html')

#if (__name__ == '__main__'):
#  app.run(debug=True)
app.run(host='localhost', port=5000, debug=True)