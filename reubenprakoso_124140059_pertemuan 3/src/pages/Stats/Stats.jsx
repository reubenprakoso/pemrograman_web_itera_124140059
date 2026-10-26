
import PropTypes from 'prop-types'
import { useBooks } from '../../context/BookContext'
import useBookStats from '../../hooks/useBookStats'

export default function Stats() {
  const { books } = useBooks()
  const stats = useBookStats(books)

  return (
    <main>
      <h1>Statistik Buku</h1>
      <p>Ringkasan koleksi buku pribadi kamu.</p>

      <section>
        <h2>Total Buku</h2>
        <p>{stats.total}</p>
      </section>

      <section>
        <h2>Sudah Dimiliki</h2>
        <p>{stats.owned}</p>
      </section>

      <section>
        <h2>Sedang Dibaca</h2>
        <p>{stats.reading}</p>
      </section>

      <section>
        <h2>Ingin Dibeli</h2>
        <p>{stats.wantToBuy}</p>
      </section>
    </main>
  )
}

Stats.propTypes = {}
