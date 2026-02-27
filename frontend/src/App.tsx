import { useEffect, useState } from 'react'
import './App.css'

const API_BASE = "http://localhost:8000"

function App() {
  const [count, setCount] = useState<number>(0)
  const [loading, setLoading] = useState<boolean>(false)

  // Fetch initial count on component mount
  useEffect(() => {
    fetch(`${API_BASE}/count`)
      .then(res => res.json())
      .then(data => {
        setCount(data.count)
      })
      .catch(err => {
        console.error("Error fetching count:", err)
      })
  }, [])

  // Call FastAPI increment endpoint
  const handleIncrement = async () => {
    try {
      setLoading(true)

      const response = await fetch(`${API_BASE}/increment`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        }
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
    <>
      <h1>Vite + React + FastAPI</h1>

      <div className="card">
        <button onClick={handleIncrement} disabled={loading}>
          {loading ? "Updating..." : `count is ${count}`}
        </button>
      </div>
    </>
  )
}

export default App