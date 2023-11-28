import mysql.connector

userName = input(str("Digite seu usuário:"))
emailUser = input(str("Digite um email:"))
senhaUser = input(str("Digite uma senha:"))

class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Interprise:
    def __init__(self, nomeEmpresa, cpnj, endereco):
        self.nomeEmpresa = nomeEmpresa
        self.cpnj = cpnj
        self.endereco = endereco

dbMundMart = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'dbMundMart'
)

mycursor = dbMundMart.cursor()

sql = "INSERT INTO usuario(nome, email, senha) VALUES (%s, %s)"
dates = ('userName', 'emailUser', 'senhaUser')

mycursor.execute(sql, dates)

mycursor.execute("SELECT * FROM usuario")

myresult = mycursor.fetchall()