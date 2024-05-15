from flask import Flask, render_template  # llamar al framework

app = Flask(__name__)  # guarda en una variable la ruta de inicio de la app

# Rutas de procesamiento (direccionan a algun lugar)
@app.route('/')    # método que crea una url
def home():        # función  que devuelve información al navegador
    return "Home de Potrero Digital"

@app.route('/about')
def about():
    return "About de Potrero Digital"

# validamos si estamos en el archivo principal para que siempre se quede
# escuchando una peticion del usuario y si se cumple ejecuta el app.run
if __name__ == '__main__':
    app.run()
