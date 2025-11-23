from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    resultado=None
    if request.method=='POST':
        nombre=request.form['nombre']
        edad=int(request.form['edad'])
        qty=int(request.form['cantidad'])
        precio=9000
        total=precio*qty
        descuento=0
        if 18<=edad<=30:
            descuento=total*0.15
        elif edad>30:
            descuento=total*0.25
        total_pagar=total-descuento
        resultado={'nombre':nombre,'total':total,'descuento':descuento,'total_pagar':total_pagar}
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET','POST'])
def ejercicio2():
    mensaje=None
    users={'juan':'admin','pepe':'user'}
    if request.method=='POST':
        nombre=request.form['nombre']
        clave=request.form['clave']
        if nombre in users and users[nombre]==clave:
            if nombre=='juan':
                mensaje=f'Bienvenido Administrador {nombre}'
            else:
                mensaje=f'Bienvenido Usuario {nombre}'
        else:
            mensaje='Usuario o contraseña incorrectos'
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__=='__main__':
    app.run(debug=True)
