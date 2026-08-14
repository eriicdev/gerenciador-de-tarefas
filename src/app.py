from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Fazer trabalho de Engenharia de Software",
        "prioridade": "Alta",
        "concluida": False
    },
    {
        "id": 2,
        "titulo": "Estudar para a prova",
        "prioridade": "Média",
        "concluida": False
    }
]

PRIORIDADES_VALIDAS = {"Alta", "Média", "Baixa"}
FILTROS_VALIDOS = {"todas", "pendentes", "concluidas"}


@app.route("/")
def inicio():
    filtro = request.args.get("filtro", "todas")

    if filtro not in FILTROS_VALIDOS:
        filtro = "todas"

    if filtro == "pendentes":
        tarefas_exibidas = [
            tarefa for tarefa in tarefas
            if not tarefa["concluida"]
        ]

    elif filtro == "concluidas":
        tarefas_exibidas = [
            tarefa for tarefa in tarefas
            if tarefa["concluida"]
        ]

    else:
        tarefas_exibidas = tarefas

    return render_template(
        "index.html",
        tarefas=tarefas_exibidas,
        filtro=filtro
    )


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form.get("titulo", "").strip()
    prioridade = request.form.get("prioridade", "")

    if not titulo:
        return redirect(url_for("inicio"))

    if prioridade not in PRIORIDADES_VALIDAS:
        prioridade = "Média"

    novo_id = max([t["id"] for t in tarefas], default=0) + 1

    tarefas.append({
        "id": novo_id,
        "titulo": titulo,
        "prioridade": prioridade,
        "concluida": False
    })

    return redirect(url_for("inicio"))


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if tarefa is None:
        return redirect(url_for("inicio"))

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        prioridade = request.form.get("prioridade", "")

        if not titulo:
            return render_template(
                "editar.html",
                tarefa=tarefa,
                erro="O título da tarefa não pode ficar vazio."
            )

        if prioridade not in PRIORIDADES_VALIDAS:
            prioridade = "Média"

        tarefa["titulo"] = titulo
        tarefa["prioridade"] = prioridade

        return redirect(url_for("inicio"))

    return render_template("editar.html", tarefa=tarefa)


@app.route("/concluir/<int:id>")
def concluir(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if tarefa is not None:
        tarefa["concluida"] = not tarefa["concluida"]

    return redirect(url_for("inicio"))


@app.route("/excluir/<int:id>")
def excluir(id):
    tarefas[:] = [t for t in tarefas if t["id"] != id]

    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)