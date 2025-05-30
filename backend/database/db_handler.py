import sqlite3

class DBHandler:
    def __init__(self, db_path="ecommerce.db"):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_tables(self, schema_path="database/schema.sql"):
        with self.get_connection() as conn, open(schema_path, "r") as f:
            conn.executescript(f.read())

    def execute_query(self, query, params=(), commit=False):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if commit:
                conn.commit()
            return cursor

    def fetch_one(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchone()

    def fetch_all(self, query, params=()):
        cursor = self.execute_query(query, params)
        return cursor.fetchall()

    # Métodos específicos por entidad (ejemplo para usuarios)
    def create_user(self, name, email, password, role="customer"):
        query = "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)"
        self.execute_query(query, (name, email, password, role), commit=True)

    def get_user_by_email(self, email):
        query = "SELECT * FROM users WHERE email = ?"
        return self.fetch_one(query, (email,))

    def validate_user(self, email, password):
        user = self.get_user_by_email(email)
        if user and user[3] == password:  # Ajusta según cómo almacenes la contraseña
            return user
        return None

    # Métodos para productos y órdenes pueden agregarse de forma similar