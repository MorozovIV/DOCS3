from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html', name=index)
@app.route('/browser',methods = ['GET'])
def browser():
    return render_template('browser.html')
@app.route('/uprdor-m2',methods = ['GET'])
def uprdor():
    return render_template('uprdor-m2.html')
@app.route('/rosavtodor',methods = ['GET'])
def rosavtodor():
    return render_template('rosavtodor.html')
@app.route('/yandex',methods = ['GET'])
def yandex():
    return render_template('yandex.html')
@app.route('/asmo',methods = ['GET'])
def asmo():
    return render_template('asmo.html')
@app.route('/sedd',methods = ['GET'])
def sedd():
    return render_template('sedd.html')
@app.route('/risad_new',methods = ['GET'])
def risad_new():
    return render_template('risad_new.html')
@app.route('/risad',methods = ['GET'])
def risad():
    return render_template('risad.html')
@app.route('/roadsoft',methods = ['GET'])
def roadsoft():
    return render_template('roadsoft.html')
@app.route('/som_tesad',methods = ['GET'])
def som_tesad():
    return render_template('som_tesad.html')
@app.route('/etalon',methods = ['GET'])
def etalon():
    return render_template('etalon.html')
@app.route('/etalon_web',methods = ['GET'])
def etalon_web():
    return render_template('etalon_web.html')
@app.route('/abdd',methods = ['GET'])
def abdd():
    return render_template('abdd.html')
@app.route('/uspd',methods = ['GET'])
def uspd():
    return render_template('uspd.html')
@app.route('/web_mail',methods = ['GET'])
def web_mail():
    return render_template('web_mail.html')
@app.route('/docs',methods = ['GET'])
def docs():
    return render_template('docs.html')
@app.route('/ugiz',methods = ['GET'])
def ugiz():
    return render_template('ugiz.html')
if __name__ == '__main__':
    app.run(host='10.10.21.207', port='8080', debug=True)