import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from typing import List, Tuple, Set
import re
import webbrowser


class SistemaBuscaSRI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Recuperação de Informação")
        self.root.geometry("1400x700")  # Aumentado para acomodar mais colunas
        
        # Configuração do banco de dados
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',  # Altere conforme necessário
            'database': 'SRI'
        }
        
        self.criar_interface()
        
    def criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Título
        titulo = ttk.Label(main_frame, text="Sistema de Busca de Artigos", 
                          font=('Arial', 16, 'bold'))
        titulo.grid(row=0, column=0, pady=10)
        
        # Frame de busca
        search_frame = ttk.LabelFrame(main_frame, text="Busca", padding="10")
        search_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)
        search_frame.columnconfigure(1, weight=1)
        
        # Campo de entrada
        ttk.Label(search_frame, text="Consulta:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entrada_busca = ttk.Entry(search_frame, width=50)
        self.entrada_busca.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Tipo de busca
        ttk.Label(search_frame, text="Tipo de Busca:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.tipo_busca = tk.StringVar(value="booleana")
        
        radio_frame = ttk.Frame(search_frame)
        radio_frame.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
        ttk.Radiobutton(radio_frame, text="Booleana", variable=self.tipo_busca, 
                       value="booleana").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(radio_frame, text="Vetorial", variable=self.tipo_busca, 
                       value="vetorial").pack(side=tk.LEFT, padx=5)
        
        # Botão de busca
        ttk.Button(search_frame, text="Pesquisar", 
                  command=self.executar_busca).grid(row=2, column=1, sticky=tk.W, padx=5, pady=10)
        
        # Frame de resultados
        results_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="10")
        results_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Tabela de resultados
        self.tree = ttk.Treeview(results_frame, 
                                columns=("Rank", "Titulo", "Autores", "Filiacao", "Resumo", "Palavras_Chaves", "Link", "Score"), 
                                show="headings", height=15)
        
        self.tree.heading("Rank", text="#")
        self.tree.heading("Titulo", text="Título")
        self.tree.heading("Autores", text="Autores")
        self.tree.heading("Filiacao", text="Filiação")
        self.tree.heading("Resumo", text="Resumo")
        self.tree.heading("Palavras_Chaves", text="Palavras-Chave")
        self.tree.heading("Link", text="Link")
        self.tree.heading("Score", text="Relevância")
        
        self.tree.column("Rank", width=35)
        self.tree.column("Titulo", width=250)
        self.tree.column("Autores", width=180)
        self.tree.column("Filiacao", width=150)
        self.tree.column("Resumo", width=300)
        self.tree.column("Palavras_Chaves", width=150)
        self.tree.column("Link", width=200)
        self.tree.column("Score", width=85)
        
        # Scrollbars
        scrollbar_y = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar_x = ttk.Scrollbar(results_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar_y.grid(row=0, column=1, sticky=(tk.N, tk.S))
        scrollbar_x.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Botão detalhes
        ttk.Button(results_frame, text="Ver Detalhes", 
                  command=self.mostrar_detalhes).grid(row=2, column=0, pady=10)
        
        # Label de instrução
        instrucao = ttk.Label(results_frame, text="💡 Dica: Dê duplo clique no Link para abrir no navegador", 
                             foreground="blue", font=('Arial', 9, 'italic'))
        instrucao.grid(row=2, column=0, pady=10, padx=(200, 0), sticky=tk.W)
        
        # Bind para duplo clique e clique simples na árvore
        self.tree.bind("<Double-Button-1>", self.ao_duplo_clique)
        self.tree.bind("<Button-1>", self.ao_clicar)
        
    def conectar_bd(self):
        """Estabelece conexão com o banco de dados"""
        try:
            return mysql.connector.connect(**self.db_config)
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao banco de dados: {err}")
            return None
    
    def processar_consulta_booleana(self, consulta: str) -> Tuple[List[str], List[str]]:
        """Processa a consulta booleana separando palavras e operadores"""
        consulta = consulta.lower()
        
        # Divide a consulta em tokens
        tokens = consulta.split()
        
        palavras = []
        operadores = []
        
        for token in tokens:
            if token in ['and', 'or']:
                operadores.append(token)
            else:
                palavras.append(token)
        
        return palavras, operadores
    
    def processar_consulta_vetorial(self, consulta: str) -> List[str]:
        """Processa a consulta vetorial removendo vírgulas"""
        consulta = consulta.lower()
        # Remove vírgulas e divide em palavras
        consulta = consulta.replace(',', ' ')
        palavras = consulta.split()
        return [p.strip() for p in palavras if p.strip()]
    
    def buscar_artigos_por_termo(self, termo: str) -> Set[int]:
        """Busca artigos que contêm um termo específico"""
        conn = self.conectar_bd()
        if not conn:
            return set()
        
        try:
            cursor = conn.cursor()
            query = """
                SELECT DISTINCT d.id_artigo
                FROM documentos d
                JOIN dicionario dic ON d.id_termo = dic.id
                WHERE dic.termo = %s
            """
            cursor.execute(query, (termo,))
            resultados = cursor.fetchall()
            return set(row[0] for row in resultados)
        finally:
            cursor.close()
            conn.close()
    
    def calcular_relevancia(self, id_artigo: int, palavras: List[str]) -> float:
        """Calcula a relevância de um artigo baseado nos termos buscados usando TF-IDF"""
        conn = self.conectar_bd()
        if not conn:
            return 0.0
        
        try:
            cursor = conn.cursor()
            score = 0.0
            
            for palavra in palavras:
                query = """
                    SELECT d.tf_logaritimo * d.idf_logaritimo as tfidf
                    FROM documentos d
                    JOIN dicionario dic ON d.id_termo = dic.id
                    WHERE d.id_artigo = %s AND dic.termo = %s
                """
                cursor.execute(query, (id_artigo, palavra))
                resultado = cursor.fetchone()
                
                if resultado and resultado[0]:
                    score += resultado[0]
            
            return score
        finally:
            cursor.close()
            conn.close()
    
    def executar_busca_booleana(self, palavras: List[str], operadores: List[str]) -> Set[int]:
        """Executa busca booleana processando operadores da esquerda para direita"""
        if not palavras:
            return set()
        
        # Começa com o primeiro termo
        resultado = self.buscar_artigos_por_termo(palavras[0])
        
        # Processa cada operador com a próxima palavra
        for i, operador in enumerate(operadores):
            if i + 1 < len(palavras):
                proximos_artigos = self.buscar_artigos_por_termo(palavras[i + 1])
                
                if operador == 'and':
                    # Interseção
                    resultado = resultado.intersection(proximos_artigos)
                elif operador == 'or':
                    # União
                    resultado = resultado.union(proximos_artigos)
        
        return resultado
    
    def executar_busca_vetorial(self, palavras: List[str]) -> Set[int]:
        """Executa busca vetorial usando união de todos os termos"""
        resultado = set()
        
        for palavra in palavras:
            artigos = self.buscar_artigos_por_termo(palavra)
            resultado = resultado.union(artigos)
        
        return resultado
    
    def obter_dados_artigos(self, ids_artigos: Set[int], palavras: List[str] = None) -> List[Tuple]:
        """Obtém dados completos dos artigos com join de autores, ordenados por relevância"""
        if not ids_artigos:
            return []
        
        # Se palavras foram fornecidas, calcula relevância para ordenar
        if palavras:
            # Cria lista de tuplas (id_artigo, score)
            artigos_com_score = []
            for id_artigo in ids_artigos:
                score = self.calcular_relevancia(id_artigo, palavras)
                artigos_com_score.append((id_artigo, score))
            
            # Ordena por score (maior primeiro) e depois por ID
            artigos_com_score.sort(key=lambda x: (-x[1], x[0]))
            ids_ordenados = [id_art for id_art, _ in artigos_com_score]
            scores_dict = {id_art: score for id_art, score in artigos_com_score}
        else:
            ids_ordenados = list(ids_artigos)
            scores_dict = {id_art: 0.0 for id_art in ids_ordenados}
        
        conn = self.conectar_bd()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            
            # Cria um CASE para manter a ordem desejada
            when_clauses = ' '.join([f'WHEN {id_val} THEN {i}' for i, id_val in enumerate(ids_ordenados)])
            
            query = f"""
                SELECT 
                    a.id,
                    a.titulo,
                    GROUP_CONCAT(aut.nome ORDER BY aut.ordem SEPARATOR ', ') as autores,
                    a.filiacao,
                    a.resumo,
                    a.palavras_chaves,
                    a.link
                FROM artigos a
                LEFT JOIN autores aut ON a.id = aut.id_artigo
                WHERE a.id IN ({','.join(['%s'] * len(ids_ordenados))})
                GROUP BY a.id, a.titulo, a.filiacao, a.resumo, a.palavras_chaves, a.link
                ORDER BY CASE a.id {when_clauses} END
            """
            
            cursor.execute(query, tuple(ids_ordenados))
            resultados = cursor.fetchall()
            
            # Adiciona o score aos resultados
            resultados_com_score = []
            for row in resultados:
                id_artigo = row[0]
                score = scores_dict.get(id_artigo, 0.0)
                resultados_com_score.append(row + (score,))
            
            return resultados_com_score
        finally:
            cursor.close()
            conn.close()
    
    def executar_busca(self):
        """Executa a busca baseada no tipo selecionado"""
        consulta = self.entrada_busca.get().strip()
        
        if not consulta:
            messagebox.showwarning("Aviso", "Por favor, insira uma consulta de busca.")
            return
        
        # Limpa resultados anteriores
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        tipo = self.tipo_busca.get()
        palavras = []  # Armazena as palavras para calcular relevância
        
        if tipo == "booleana":
            palavras, operadores = self.processar_consulta_booleana(consulta)
            ids_artigos = self.executar_busca_booleana(palavras, operadores)
        else:  # vetorial
            palavras = self.processar_consulta_vetorial(consulta)
            ids_artigos = self.executar_busca_vetorial(palavras)
        
        # Obtém e exibe os resultados ordenados por relevância
        resultados = self.obter_dados_artigos(ids_artigos, palavras)
        
        if not resultados:
            messagebox.showinfo("Resultado", "Nenhum artigo encontrado.")
            return
        
        for rank, row in enumerate(resultados, start=1):
            # row = (id, titulo, autores, filiacao, resumo, palavras_chaves, link, score)
            id_artigo = row[0]
            titulo = row[1]
            autores = row[2]
            filiacao = row[3]
            resumo = row[4]
            palavras_chaves = row[5]
            link = row[6]
            score = row[7]
            
            # Insere na árvore com tags para armazenar o ID
            item_id = self.tree.insert("", tk.END, values=(
                rank,
                titulo,
                autores,
                filiacao,
                resumo,
                palavras_chaves,
                link,
                f"{score:.4f}"
            ), tags=(str(id_artigo),))
        
        messagebox.showinfo("Resultado", f"{len(resultados)} artigo(s) encontrado(s).\nOrdenados por relevância (mais relevante primeiro).")
    
    def ao_clicar(self, event):
        """Detecta clique em uma célula"""
        region = self.tree.identify_region(event.x, event.y)
        if region != "cell":
            return
        
        coluna = self.tree.identify_column(event.x)
        # Coluna 7 é o Link (índice #6 em identify_column que começa com #0)
        if coluna == "#7":  # Link column
            self.tree.config(cursor="hand2")
        else:
            self.tree.config(cursor="")
    
    def ao_duplo_clique(self, event):
        """Abre o link quando duplo clique na coluna Link"""
        region = self.tree.identify_region(event.x, event.y)
        if region != "cell":
            return
        
        coluna = self.tree.identify_column(event.x)
        item = self.tree.identify_row(event.y)
        
        if not item:
            return
        
        # Coluna 7 é o Link
        if coluna == "#7":  # Link column
            valores = self.tree.item(item)['values']
            link = valores[6]  # Link está na posição 6
            
            if link:
                try:
                    webbrowser.open(link)
                    messagebox.showinfo("Link", f"Abrindo: {link}")
                except Exception as e:
                    messagebox.showerror("Erro", f"Não foi possível abrir o link: {e}")
    
    def mostrar_detalhes(self):
        """Mostra os detalhes do artigo selecionado"""
        selecionado = self.tree.selection()
        
        if not selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione um artigo.")
            return
        
        # Obtém o ID do artigo selecionado das tags
        item = self.tree.item(selecionado[0])
        id_artigo = int(item['tags'][0])  # O ID está armazenado nas tags
        
        # Cria janela de detalhes
        self.janela_detalhes = tk.Toplevel(self.root)
        self.janela_detalhes.title(f"Detalhes do Artigo - ID: {id_artigo}")
        self.janela_detalhes.geometry("800x500")
        
        # Frame principal
        frame = ttk.Frame(self.janela_detalhes, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(frame, text=f"Termos do Artigo ID: {id_artigo}", 
                 font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Tabela de termos
        tree_detalhes = ttk.Treeview(frame, columns=("Termo", "TF", "IDF"), 
                                     show="headings", height=20)
        
        tree_detalhes.heading("Termo", text="Termo")
        tree_detalhes.heading("TF", text="TF (log)")
        tree_detalhes.heading("IDF", text="IDF (log)")
        
        tree_detalhes.column("Termo", width=400)
        tree_detalhes.column("TF", width=150)
        tree_detalhes.column("IDF", width=150)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree_detalhes.yview)
        tree_detalhes.configure(yscrollcommand=scrollbar.set)
        
        tree_detalhes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Busca os detalhes no banco
        conn = self.conectar_bd()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            query = """
                SELECT 
                    dic.termo,
                    d.tf_logaritimo,
                    d.idf_logaritimo
                FROM documentos d
                JOIN dicionario dic ON d.id_termo = dic.id
                WHERE d.id_artigo = %s
                ORDER BY dic.termo
            """
            cursor.execute(query, (id_artigo,))
            resultados = cursor.fetchall()
            
            for row in resultados:
                tree_detalhes.insert("", tk.END, values=(
                    row[0],
                    f"{row[1]:.4f}",
                    f"{row[2]:.4f}"
                ))
        finally:
            cursor.close()
            conn.close()


def main():
    root = tk.Tk()
    app = SistemaBuscaSRI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
