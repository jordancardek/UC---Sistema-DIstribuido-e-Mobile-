from flask import Flask, request, render_template
from datetime import date
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

@app.route('/produtos/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        descricao = request.form['descricao']
        precocompra = request.form['precocompra']
        precovenda = request.form['precovenda']
        datacriacao = date.today()

        if descricao and precocompra and precovenda:
            registro = (descricao, precocompra, precovenda, datacriacao)

            try:
                conn = sqlite3.connect("C:/Users/Koda/Desktop/UC---Sistema-DIstribuido-e-Mobile-/Prática 04/db-produtos.db")
                sql = '''INSERT INTO produtos(descricao, precocompra, precovenda, datacriacao) 
                         VALUES(?,?,?,?)'''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()
            except Error as e:
                print(e)
            finally:
                conn.close()

    return render_template('cadastrar.html')

@app.route('/produtos/listar', methods=['GET'])
def listar():
    try:
        conn = sqlite3.connect('database/db-produtos.db')
        sql = '''SELECT * FROM produtos'''
        cur = conn.cursor()
        cur.execute(sql)
        registros = cur.fetchall()
        return render_template('listar.html', regs=registros)
    except Error as e:
        print(e)
    finally:
        conn.close()

@app.route('/produtos/excluir/<int:idproduto>', methods=['GET'])
def excluir(idproduto):
    try:
        conn = sqlite3.connect('database/db-produtos.db')
        sql = '''DELETE FROM produtos WHERE idproduto = ?'''
        cur = conn.cursor()
        cur.execute(sql, (idproduto,))
        conn.commit()
    except Error as e:
        print(e)
    finally:
        conn.close()

    return "Produto excluído com sucesso!"

@app.route('/produtos/editar/<int:idproduto>', methods=['GET', 'POST'])
def editar(idproduto):
    conn = sqlite3.connect('database/db-produtos.db')
    cur = conn.cursor()

    if request.method == 'POST':
        descricao = request.form['descricao']
        precocompra = request.form['precocompra']
        precovenda = request.form['precovenda']

        sql = '''UPDATE produtos 
                 SET descricao=?, precocompra=?, precovenda=?
                 WHERE idproduto=?'''
        cur.execute(sql, (descricao, precocompra, precovenda, idproduto))
        conn.commit()
        conn.close()
        return "Produto alterado com sucesso!"

    sql = '''SELECT * FROM produtos WHERE idproduto=?'''
    cur.execute(sql, (idproduto,))
    produto = cur.fetchone()
    conn.close()

    return render_template('editar.html', produto=produto)

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)