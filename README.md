# GEMA
> Gestão de Equipamentos e Manutenção

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-blue" alt="Status do Projeto">
  <img src="https://img.shields.io/badge/licen%C3%A7a-MIT-green" alt="Licença">
</p>

## 📝 Sobre o Projeto

**GEMA (Gestão de Equipamentos e Manutenção)** é um sistema focado em otimizar e organizar o ciclo de vida de ativos e equipamentos. 

O objetivo principal é centralizar o registro de manutenções, controlar a disponibilidade de equipamentos em tempo real e agilizar a tomada de decisão para equipes de operação e manutenção, reduzindo o tempo de inatividade e aumentando a eficiência operacional.

---

## ✨ Funcionalidades Principais

* **📋 Cadastro de Ativos:** Inventário centralizado de todos os equipamentos, com detalhes, especificações e localização.
* **🛠️ Ordens de Serviço (OS):** Criação, gestão e rastreamento de manutenções corretivas e preventivas.
* **🟢 Status em Tempo Real:** Dashboard visual para identificar rapidamente quais equipamentos estão **disponíveis**, **em uso**, **em manutenção** ou **inoperantes**.
* **📊 Histórico e Relatórios:** Acesso fácil ao histórico completo de cada ativo, permitindo auditorias e análises de custo e performance.

---

## 💻 Tecnologias Utilizadas

Esta seção descreve as principais tecnologias usadas no desenvolvimento do GEMA.

* **Linguagem:** Python
* **Interface Gráfica (GUI):** Tkinter
* **Banco de Dados:** MongoDB (com PyMongo para conexão)

---

## 🚀 Como Começar (Instalação e Uso)

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

* Você precisa ter o **Python 3.13.9** instalado.
* Você precisa ter o **MongoDB** instalado e rodando em sua máquina.
    * [Guia de Instalação do MongoDB](https://docs.mongodb.com/manual/installation/)

### Guia de Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/ViniciusMakimoto/GEMA.git
    ```

2.  Navegue até o diretório do projeto:
    ```bash
    cd GEMA
    ```

3.  Crie e ative um ambiente virtual (recomendado para projetos Python):
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

4.  Instale as dependências Python:
    ```bash
    pip install -r requirements.txt
    ```
    * **Nota:** Certifique-se de que o arquivo `requirements.txt` existe e lista as dependências como `Pillow` (para imagens, se usar), `pymongo` (para MongoDB), etc. Se não tiver, crie-o com `pip freeze > requirements.txt` após instalar suas bibliotecas.
    * 
5.  Inicie a aplicação:
    ```bash
    python main.py 
    ```

---

## 🤝 Como Contribuir

Contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

1.  Faça um **Fork** do projeto.
2.  Crie uma nova Branch para sua feature (`git checkout -b feature/MinhaNovaFeature`).
3.  Faça o **Commit** das suas alterações (`git commit -m 'Adiciona MinhaNovaFeature'`).
4.  Faça o **Push** para a Branch (`git push origin feature/MinhaNovaFeature`).
5.  Abra um **Pull Request**.

---
<p align="center">
  Feito com ❤️ por:
</p>
<p align="center">
  Vinícius Makimoto de Freitas
</p>
<p align="center">
  Carlos Eduardo Gatto
</p>
<p align="center">
  Yago Patrick Gomide Olivera Ortolan
</p>
<p align="center">
  Luiz Felipe Farias Mota
</p>
<p align="center">
  Raphaella Souza de Moraes
</p>
