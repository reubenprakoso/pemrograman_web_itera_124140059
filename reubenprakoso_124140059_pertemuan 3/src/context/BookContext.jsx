
import { createContext, useContext } from 'react'
import PropTypes from 'prop-types'
import useLocalStorage from '../hooks/useLocalStorage'

const BookContext = createContext(null)

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('manajemen-buku', [])

  function addBook(book) {
    setBooks((currentBooks) => [
      ...currentBooks,
      { ...book, id: crypto.randomUUID() },
    ])
  }

  function updateBook(id, updatedData) {
    setBooks((currentBooks) =>
      currentBooks.map((book) =>
        book.id === id ? { ...book, ...updatedData } : book,
      ),
    )
  }

  function deleteBook(id) {
    setBooks((currentBooks) =>
      currentBooks.filter((book) => book.id !== id),
    )
  }

  return (
    <BookContext.Provider
      value={{ books, addBook, updateBook, deleteBook }}
    >
      {children}
    </BookContext.Provider>
  )
}

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
}

export function useBooks() {
  const context = useContext(BookContext)

  if (!context) {
    throw new Error('useBooks harus digunakan di dalam BookProvider')
  }

  return context
}
