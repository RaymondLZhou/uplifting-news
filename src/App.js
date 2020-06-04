import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'
import feed from './scraper/feed.json'
import Card from 'react-bootstrap/Card'
import CardColumns from 'react-bootstrap/CardColumns'

const display = feed.map((feed) => {
  return (
    <Card style={{ width: '35rem' }} className="card">
      <Card.Body>
        <Card.Title> 
          {feed.title} 
        </Card.Title>
        
        <Card.Text>
          {feed.description}
        </Card.Text>

        <Card.Text>
          {feed.date}
        </Card.Text>

        <Card.Text>
          <a 
            href={feed.link} 
            className="App-link" 
            target="_blank"
            rel="noopener noreferrer"
          >
              Link to Article
          </a>
        </Card.Text>
      </Card.Body>
    </Card>
  )
})

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />

        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        <Link to="/second-page">
          <button className="button" id="spaces">
           Link to Second Page
          </button>
        </Link>

        <CardColumns> {display} </CardColumns>
      </header>
    </div>
  )
}

export default App
