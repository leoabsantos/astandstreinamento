from flask import Flask, render_template
app = Flask(__name__)
#criar a 1ª Pagina do site
#route -> astandstreinamentos.com/contatos
#funcao -> o que vc quer exibir naquela página
#template
@app.route("/") #pagina principal home page
def homepage():
    return render_template("homepage.html")

@app.route("/colaboradores") #pagina colaboradores
def colaboradores():
    return render_template("colaboradores.html")

@app.route("/contatos") #pagina contatos
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios") #pagina lista os usuarios
def usuarios():
    return render_template("usuarios.html")

@app.route("/perfil_usuarios") #pagina perfil de usuarios
def perfil_usuarios():
    return render_template("perfil_usuarios.html")

#@app.route("/usuarios/<nome_usuario>") #pagina cria a página do usuario
#def usuarios_perfil(nome_usuario):
 #  return nome_usuario

@app.route("/usuarios/<nome_usuario>")
def usuarios1(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)
#se eu quiser pegar uma informação dinamica que está dentro de um link e passar para minha página tenho que fazer 4 passos
#passo 1 - no link colocar a variavel entre chaves
#Passo 2 - colocar o mesmo nome da variavel como parâmetro sendo uma variavel
#Passo 3 - dentro do render_template coloca variavel igual a variavel repete o mesmo nome
#Passo 4 - posso usar a variavel dentro do html como eu quiser

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

#servidor do heroku