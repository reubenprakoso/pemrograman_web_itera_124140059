
import PropTypes from 'prop-types'

export default function BookFilter({
  search,
  onSearchChange,
  statusFilter,
  onStatusChange,
}) {
  return (
    <section>
      <h2>Cari dan Filter Buku</h2>

      <div>
        <label htmlFor="book-search">Cari Buku</label>
        <input
          id="book-search"
          type="text"
          value={search}
          onChange={(event) => onSearchChange(event.target.value)}
          placeholder="Cari judul atau nama penulis"
        />
      </div>

      <div>
        <label htmlFor="status-filter">Filter Status</label>
        <select
          id="status-filter"
          value={statusFilter}
          onChange={(event) => onStatusChange(event.target.value)}
        >
          <option value="all">Semua Buku</option>
          <option value="owned">Sudah Dimiliki</option>
          <option value="reading">Sedang Dibaca</option>
          <option value="want to buy">Ingin Dibeli</option>
        </select>
      </div>
    </section>
  )
}

BookFilter.propTypes = {
  search: PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired,
  statusFilter: PropTypes.string.isRequired,
  onStatusChange: PropTypes.func.isRequired,
}
