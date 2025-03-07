import sqlite3
import os

# Database connection
DB_FILE = "notes.db"

def connect_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn

def create_note(title, content):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()
    print("Note added successfully.")

def view_notes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content, created_at FROM notes")
    notes = cursor.fetchall()
    conn.close()
    
    if not notes:
        print("No notes found.")
    else:
        for note in notes:
            print(f"{note[0]}. {note[1]} - {note[2]} (Created: {note[3]})")

def update_note(note_id, new_title, new_content):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET title=?, content=? WHERE id=?", (new_title, new_content, note_id))
    conn.commit()
    conn.close()
    print("Note updated successfully.")

def delete_note(note_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()
    print("Note deleted successfully.")

# Menu-driven program
if __name__ == "__main__":
    while True:
        print("\nPersonal Note-Taking App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            create_note(title, content)
        elif choice == "2":
            view_notes()
        elif choice == "3":
            note_id = int(input("Enter note ID to update: "))
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            update_note(note_id, new_title, new_content)
        elif choice == "4":
            note_id = int(input("Enter note ID to delete: "))
            delete_note(note_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
