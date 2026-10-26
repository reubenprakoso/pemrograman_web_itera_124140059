
import { useState } from 'react'
import PropTypes from 'prop-types'

export default function BookList({ books, onDeleteBook, onEditBook }) {
  const [editingId, setEditingId] = useState(null)
  const [title, setTitle] = useState('')
  const [author, setAuthor] = useState('')
  const [status, setStatus] = useState('owned')
  const [error, setError] = useState('')

  function startEditing(book) {
    setEditingId(book.id)
    setTitle(book.title)
    setAuthor(book.author)
    setStatus(book.status)
    setError('')
  }

  function handleSave(id) {
    if (!title.trim() || !author.trim()) {
      setError('Judul dan nama penulis wajib diisi.')
      return
    }

    onEditBook(id, {
      title: title.trim(),
      author: author.trim(),
      status,
    })

    setEditingId(null)
    setError('')
  }

  if (books.length === 0) {
    return <p>Belum ada buku. Silakan tambahkan buku baru.</p>
  }

  return (
    <section>
      <h2>Daftar Buku</h2>

      {books.map((book) => (
        <article key={book.id}>
          {editingId === book.id ? (
            <div>
              <label htmlFor={`edit-title-${book.id}`}>
                Judul Buku
              </label>
              <input
                id={`edit-title-${book.id}`}
                value={title}
                onChange={(event) => setTitle(event.target.value)}
              />

              <label htmlFor={`edit-author-${book.id}`}>
                Nama Penulis
              </label>
              <input
                id={`edit-author-${book.id}`}
                value={author}
                onChange={(event) => setAuthor(event.target.value)}
              />

              <label htmlFor={`edit-status-${book.id}`}>
                Status Buku
              </label>
              <select
                id={`edit-status-${book.id}`}
                value={status}
                onChange={(event) => setStatus(event.target.value)}
              >
                <option value="owned">Sudah Dimiliki</option>
                <option value="reading">Sedang Dibaca</option>
                <option value="want to buy">Ingin Dibeli</option>
              </select>

              {error && <p role="alert">{error}</p>}

              <button type="button" onClick={() => handleSave(book.id)}>
                Simpan Perubahan
              </button>

              <button
                type="button"
                onClick={() => {
                  setEditingId(null)
                  setError('')
                }}
              >
                Batal
              </button>
            </div>
          ) : (
            <div>
              <h3>{book.title}</h3>
              <p>Penulis: {book.author}</p>
              <p>
                Status:{' '}
                {book.status === 'owned'
                  ? 'Sudah Dimiliki'
                  : book.status === 'reading'
                    ? 'Sedang Dibaca'
                    : 'Ingin Dibeli'}
              </p>

              <button
                type="button"
                onClick={() => startEditing(book)}
              >
                Edit
              </button>

              <button
                type="button"
                onClick={() => onDeleteBook(book.id)}
              >
                Hapus
              </button>
            </div>
          )}
        </article>
      ))}
    </section>
  )
}

BookList.propTypes = {
  books: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.string.isRequired,
      title: PropTypes.string.isRequired,
      author: PropTypes.string.isRequired,
      status: PropTypes.oneOf([
        'owned',
        'reading',
        'want to buy',
      ]).isRequired,
    }),
  ).isRequired,
  onDeleteBook: PropTypes.func.isRequired,
  onEditBook: PropTypes.func.isRequired,
}
