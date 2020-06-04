import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'

function SecondPage() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />

        <p>
          This is a Second Page!
        </p>

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        <Link to="/">
          <button className="button" id="spaces">
           Link to First Page
          </button>
        </Link>
      </header>
    </div>
  )
}

export default SecondPage
