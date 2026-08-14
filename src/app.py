from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Fazer trabalho de Engenharia de Software",
        "prioridade": "Alta"
    },
    {
        "id": 2,
        "titulo": "Estudar para a prova",
        "prioridade": "Média"
    }
]


@app.route("/")
def inicio():
    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form["titulo"]
    prioridade = request.form["prioridade"]

    novo_id = max([t["id"] for t in tarefas], default=0) + 1

    tarefas.append({
        "id": novo_id,
        "titulo": titulo,
        "prioridade": prioridade
    })

    return redirect(url_for("inicio"))


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if tarefa is None:
        return redirect(url_for("inicio"))

    if request.method == "POST":
        tarefa["titulo"] = request.form["titulo"]
        tarefa["prioridade"] = request.form["prioridade"]

        return redirect(url_for("inicio"))

    return render_template("editar.html", tarefa=tarefa)


@app.route("/excluir/<int:id>")
def excluir(id):
    global tarefas

    tarefas = [t for t in tarefas if t["id"] != id]

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)