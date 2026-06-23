from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    aluno = {
        "nome": "Pedro Nagy",
        "Turma": "1 Ensino Médio Tecnico"
    }
    professores = [
        {
            "nome": "Felipe Ishara";
            "material": "Web"   
        },
            "nome": "Edidio"
            "material": "Software"
            }  
    ]
    return render_template('index.html', title="home")

@app.route("/boletim")
def boletim():
    return render_template('boletim.html', titz\le="boletim")
