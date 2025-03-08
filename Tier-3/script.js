function fetchNotes() {
    fetch('/notes')
        .then(response => response.json())
        .then(data => {
            const notesList = document.getElementById('notesList');
            notesList.innerHTML = '';
            data.forEach(note => {
                const li = document.createElement('li');
                li.innerHTML = `${note.id}: ${note.content}`;
                notesList.appendChild(li);
            });
        });
}

function addNote() {
    const noteInput = document.getElementById('noteInput');
    const content = noteInput.value.trim();
    if (content) {
        fetch('/add', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ content })
        }).then(() => {
            noteInput.value = '';
            fetchNotes();
        });
    }
}

function updateNote() {
    const id = document.getElementById('updateId').value;
    const content = document.getElementById('updateContent').value.trim();
    if (id && content) {
        fetch(`/update/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ content })
        }).then(() => {
            fetchNotes();
        });
    }
}

function deleteNote() {
    const id = document.getElementById('deleteId').value;
    if (id) {
        fetch(`/delete/${id}`, { method: 'DELETE' })
            .then(() => fetchNotes());
    }
}

document.addEventListener('DOMContentLoaded', fetchNotes);
