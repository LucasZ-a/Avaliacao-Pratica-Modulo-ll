def create_table(conn):
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                email TEXT NOT NULL
            )
        """)

def insert_aluno(conn, nome, idade, email):
    with conn:
        conn.execute(
            "INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)",
            (nome, idade, email),
        )

def list_alunos(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM alunos")
    rows = cur.fetchall()
    cur.close()

    print("■ LISTAR TODOS")
    for r in rows:
        print(r)
    if not rows:
        print("(sem registros)")
    print("-" * 50)


def get_aluno_by_id(conn, aluno_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
    row = cur.fetchone()
    cur.close()

    print(f"■ BUSCAR POR ID (id={aluno_id}) ->", row)
    print("-" * 50)
    return row


def update_aluno(conn, aluno_id, nome=None, idade=None, email=None):
    campos = []
    valores = []
    if nome is not None:
        campos.append("nome = ?")
        valores.append(nome)
    if idade is not None:
        campos.append("idade = ?")
        valores.append(idade)
    if email is not None:
        campos.append("email = ?")
        valores.append(email)

    if not campos:
        print("Nenhum campo para atualizar.")
        return

    valores.append(aluno_id)

    sql = f"UPDATE alunos SET {', '.join(campos)} WHERE id = ?"

    with conn:
        conn.execute(sql, tuple(valores))

    print(f"✏■ ATUALIZAR (id={aluno_id})")
    get_aluno_by_id(conn, aluno_id)

def delete_aluno(conn, aluno_id):
    with conn:
        conn.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
    print(f"■■ DELETAR (id={aluno_id}) concluído.")
    print("-"*50)
