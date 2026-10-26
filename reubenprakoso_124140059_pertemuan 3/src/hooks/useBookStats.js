
import { useMemo } from 'react'

export default function useBookStats(books) {
  return useMemo(() => {
    return {
      total: books.length,
      owned: books.filter((book) => book.status === 'owned').length,
      reading: books.filter((book) => book.status === 'reading').length,
      wantToBuy: books.filter(
        (book) => book.status === 'want to buy',
      ).length,
    }
  }, [books])
}
