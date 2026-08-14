import sys
from pathlib import Path

import pytest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent / "src")
)

from app import app, tarefas


@pytest.fixture
def cliente():
    app.config["TESTING"] = True

    tarefas.clear()

    tarefas.extend([
        {
            "id": 1,
            "titulo": "Tarefa de teste",
            "prioridade": "Alta",
            "concluida": False
        }
    ])

    with app.test_client() as cliente:
        yield cliente


def test_pagina_inicial(cliente):
    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert b"Tarefa de teste" in resposta.data


def test_adicionar_tarefa(cliente):
    resposta = cliente.post(
        "/adicionar",
        data={
            "titulo": "Nova tarefa",
            "prioridade": "Média"
        }
    )

    assert resposta.status_code == 302
    assert len(tarefas) == 2
    assert tarefas[1]["titulo"] == "Nova tarefa"
    assert tarefas[1]["prioridade"] == "Média"


def test_adicionar_tarefa_sem_titulo(cliente):
    resposta = cliente.post(
        "/adicionar",
        data={
            "titulo": "",
            "prioridade": "Alta"
        }
    )

    assert resposta.status_code == 302
    assert len(tarefas) == 1


def test_editar_tarefa(cliente):
    resposta = cliente.post(
        "/editar/1",
        data={
            "titulo": "Tarefa modificada",
            "prioridade": "Baixa"
        }
    )

    assert resposta.status_code == 302
    assert tarefas[0]["titulo"] == "Tarefa modificada"
    assert tarefas[0]["prioridade"] == "Baixa"


def test_concluir_tarefa(cliente):
    resposta = cliente.get("/concluir/1")

    assert resposta.status_code == 302
    assert tarefas[0]["concluida"] is True


def test_reabrir_tarefa(cliente):
    tarefas[0]["concluida"] = True

    resposta = cliente.get("/concluir/1")

    assert resposta.status_code == 302
    assert tarefas[0]["concluida"] is False


def test_excluir_tarefa(cliente):
    resposta = cliente.get("/excluir/1")

    assert resposta.status_code == 302
    assert len(tarefas) == 0