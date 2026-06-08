import { useState } from 'react'
import './App.css'

function App() {
  const [items, setItems] = useState([])
  const [status, setStatus] = useState('idle')

  const loadItems = async () => {
    setStatus('loading')

    try {
      const response = await fetch('/api/items')
      const data = await response.json()
      setItems(data)
      setStatus('success')
    } catch {
      setItems([])
      setStatus('error')
    }
  }

  return (
    <main id="center">
      <section className="hero">
        <h1>FastAPI + Vite</h1>
        <p>
          The frontend runs on Vite, and requests to <code>/api</code> are proxied to
          FastAPI.
        </p>
        <button type="button" className="counter" onClick={loadItems}>
          {status === 'loading' ? 'Loading items...' : 'Load items'}
        </button>
        {status === 'error' ? <p>Unable to reach the FastAPI backend.</p> : null}
        {items.length > 0 ? (
          <ul>
            {items.map((item) => (
              <li key={item.id}>{item.name}</li>
            ))}
          </ul>
        ) : null}
      </section>
    </main>
  )
}

export default App
