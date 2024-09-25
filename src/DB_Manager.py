import pyodbc

class DBManager:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def insert_products(self, produtos):
        conn = pyodbc.connect(self.connection_string)
        cursor = conn.cursor()

        for product in produtos:
            cursor.execute("""
                INSERT INTO STG.Produtos (Produto, Preco, Loja, NotaAvaliacao, QtdeAvaliacao, Frete, ImagemLink, ProdutoLink)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, product['produto'], product['preco'], product['loja'], product['nota_avaliacao'], 
            product['qtde_avaliacao'], product['frete'], product['imagem_link'], product['produto_link'])

        conn.commit()
        cursor.close()
        conn.close()
