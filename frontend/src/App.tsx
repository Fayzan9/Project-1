import { useEffect, useState } from 'react'
import './App.css'

const API_BASE = "http://localhost:8000"

function App() {
  const [count, setCount] = useState<number>(0)
  const [loading, setLoading] = useState<boolean>(false)

  useEffect(() => {
    fetch(`${API_BASE}/count`)
      .then(res => res.json())
      .then(data => setCount(data.count))
      .catch(err => console.error("Error fetching count:", err))
  }, [])

  const handleIncrement = async () => {
    try {
      setLoading(true)
      const response = await fetch(`${API_BASE}/increment`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
      })
      const data = await response.json()
      setCount(data.count)
    } catch (error) {
      console.error("Error incrementing count:", error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <div className="card">
        <h1 className="title">Counter Dashboard</h1>
        <p className="subtitle">Connected to FastAPI backend</p>

        <div className="count-display">
          {count}
        </div>

        <button 
          className="primary-btn"
          onClick={handleIncrement}
          disabled={loading}
        >
          {loading ? "Updating..." : "Increment"}
        </button>
      </div>
    </div>
  )
}

export default App