import sqlite3

DB_FILE = "notes.db"

def connect_db():
    """Connect to SQLite database."""
    return sqlite3.connect(DB_FILE)

def create_note(title, content):
    """Insert a new note into the database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()
    print("✅ Note added successfully.")

def view_notes():
    """Retrieve and display all notes."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content, created_at FROM notes")
    notes = cursor.fetchall()
    conn.close()

    if not notes:
        print("📂 No notes found.")
    else:
        for note in notes:
            print(f"{note[0]}. {note[1]} - {note[2]} (Created: {note[3]})")

def update_note(note_id, new_title, new_content):
    """Update an existing note by ID."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET title=?, content=? WHERE id=?", (new_title, new_content, note_id))
    conn.commit()
    conn.close()
    print("✏️ Note updated successfully.")

def delete_note(note_id):
    """Delete a note by ID."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()
    print("🗑️ Note deleted successfully.")

# Menu-driven program
if __name__ == "__main__":
    while True:
        print("\n📒 Personal Note-Taking App")
        print("1️⃣ Add Note")
        print("2️⃣ View Notes")
        print("3️⃣ Update Note")
        print("4️⃣ Delete Note")
        print("5️⃣ Exit")

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
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")
