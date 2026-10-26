
import { useState } from 'react'
import BookForm from '../../components/BookForm/BookForm'
import BookList from '../../components/BookList/BookList'
import BookFilter from '../../components/BookFilter/BookFilter'
import { useBooks } from '../../context/BookContext'

export default function Home() {
  const { books, addBook, updateBook, deleteBook } = useBooks()

  const [search, setSearch] = useState('')
  const [statusFilter, setStatusFilter] = useState('all')

  const filteredBooks = books.filter((book) => {
    const keyword = search.toLowerCase()

    const matchesSearch =
      book.title.toLowerCase().includes(keyword) ||
      book.author.toLowerCase().includes(keyword)

    const matchesStatus =
      statusFilter === 'all' || book.status === statusFilter

    return matchesSearch && matchesStatus
  })

  return (
    <main>
      <h1>Manajemen Buku Pribadi</h1>
      <p>Catat dan kelola koleksi buku kamu di sini.</p>

      <BookForm onAddBook={addBook} />

      <BookFilter
        search={search}
        onSearchChange={setSearch}
        statusFilter={statusFilter}
        onStatusChange={setStatusFilter}
      />

      <BookList
        books={filteredBooks}
        onDeleteBook={deleteBook}
        onEditBook={updateBook}
      />
    </main>
  )
}
