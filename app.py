from flask import Flask, render_template, request, redirect, url_for
from models import db, Note

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category')
        pinned = request.form.get('pinned') == 'on'

        new_note = Note(title=title, content=content, category=category, pinned=pinned)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('home'))
    
    search_query = request.args.get('search', '').strip()
    if search_query:
        notes = Note.query.filter(
            Note.title.contains(search_query) |
            Note.content.contains(search_query) |
            Note.category.contains(search_query)
        ).order_by(Note.created_at.desc()).all()
    else:
        notes = Note.query.order_by(
            Note.pinned.desc(),
            Note.created_at.desc()
        ).all()
    return render_template('index.html', notes=notes, search_query=search_query)

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        note.category = request.form.get('category')
        note.pinned = request.form.get('pinned') == 'on'
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', note=note)

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


