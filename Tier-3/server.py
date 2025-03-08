import http.server
import socketserver
import json
import sqlite3

PORT = 8001
DB_FILE = "notes.db"

# Database setup
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

class NotesHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/notes":
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notes")
            notes = [{"id": row[0], "content": row[1]} for row in cursor.fetchall()]
            conn.close()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(notes).encode())
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/add":
            content_length = int(self.headers["Content-Length"])
            post_data = json.loads(self.rfile.read(content_length))
            note_content = post_data.get("content", "")
            if note_content:
                conn = sqlite3.connect(DB_FILE)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO notes (content) VALUES (?)", (note_content,))
                conn.commit()
                conn.close()
                self.send_response(201)
                self.end_headers()
            else:
                self.send_response(400)
                self.end_headers()

    def do_PUT(self):
        if self.path.startswith("/update/"):
            note_id = self.path.split("/")[-1]
            content_length = int(self.headers["Content-Length"])
            post_data = json.loads(self.rfile.read(content_length))
            new_content = post_data.get("content", "")
            if new_content:
                conn = sqlite3.connect(DB_FILE)
                cursor = conn.cursor()
                cursor.execute("UPDATE notes SET content = ? WHERE id = ?", (new_content, note_id))
                conn.commit()
                conn.close()
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(400)
                self.end_headers()

    def do_DELETE(self):
        if self.path.startswith("/delete/"):
            note_id = self.path.split("/")[-1]
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
            conn.commit()
            conn.close()
            self.send_response(200)
            self.end_headers()

if __name__ == "__main__":
    init_db()
    with socketserver.TCPServer(("", PORT), NotesHandler) as httpd:
        print(f"Server running on port {PORT}")
        httpd.serve_forever()