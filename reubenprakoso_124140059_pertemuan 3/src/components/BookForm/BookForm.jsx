
import { useState } from 'react'
import PropTypes from 'prop-types'

export default function BookForm({ onAddBook }) {
  const [title, setTitle] = useState('')
  const [author, setAuthor] = useState('')
  const [status, setStatus] = useState('owned')
  const [error, setError] = useState('')

  function handleSubmit(event) {
    event.preventDefault()

    if (!title.trim() || !author.trim()) {
      setError('Judul dan nama penulis wajib diisi.')
      return
    }

    onAddBook({
      title: title.trim(),
      author: author.trim(),
      status,
    })

    setTitle('')
    setAuthor('')
    setStatus('owned')
    setError('')
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Tambah Buku</h2>

      <div>
        <label htmlFor="book-title">Judul Buku</label>
        <input
          id="book-title"
          type="text"
          value={title}
          onChange={(event) => setTitle(event.target.value)}
          placeholder="Masukkan judul buku"
        />
      </div>

      <div>
        <label htmlFor="book-author">Nama Penulis</label>
        <input
          id="book-author"
          type="text"
          value={author}
          onChange={(event) => setAuthor(event.target.value)}
          placeholder="Masukkan nama penulis"
        />
      </div>

      <div>
        <label htmlFor="book-status">Status Buku</label>
        <select
          id="book-status"
          value={status}
          onChange={(event) => setStatus(event.target.value)}
        >
          <option value="owned">Sudah Dimiliki</option>
          <option value="reading">Sedang Dibaca</option>
          <option value="want to buy">Ingin Dibeli</option>
        </select>
      </div>

      {error && <p role="alert">{error}</p>}

      <button type="submit">Tambah Buku</button>
    </form>
  )
}

BookForm.propTypes = {
  onAddBook: PropTypes.func.isRequired,
}
