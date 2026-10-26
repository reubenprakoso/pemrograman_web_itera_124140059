
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home/Home'
import Stats from './pages/Stats/Stats'
import './App.css'

export default function App() {
  return (
    <BrowserRouter>
      <header>
        <h1>Manajemen Buku Pribadi</h1>

        <nav>
          <Link to="/">Beranda</Link>
          {' | '}
          <Link to="/stats">Statistik Buku</Link>
        </nav>
      </header>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/stats" element={<Stats />} />
      </Routes>
    </BrowserRouter>
  )
}
