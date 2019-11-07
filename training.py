from flask import render_template
import connexion

# connexion uses flask under the covers - create a connexion app rather than flask
#  and import the swagger definition
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def training():
  return render_template('home.html')

#if (__name__ == '__main__'):
#  app.run(debug=True)
app.run(host='localhost', port=5000, debug=False)