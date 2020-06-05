import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'
import feed from './scraper/feed.json'
import Card from 'react-bootstrap/Card'
import CardColumns from 'react-bootstrap/CardColumns'

const display = feed.map((feed) => {
  return (
    <Card style={{ width: '23rem' }} className="card">
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
       
          <a
            style={{ marginLeft: '6rem' }} 
            href="#top" 
            className="App-link" 
            rel="noopener noreferrer"
          >
              Back to Top
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
        <a name="top"></a>
        <img src={logo} className="App-logo" alt="logo"/>

        <p>
          Uplifting News
        </p>

        <Link to="/second-page">
          <button className="button">
           Link to Second Page
          </button>
        </Link>

        <CardColumns className="cardColumn"> {display} </CardColumns>
      </header>
    </div>
  )
}

export default App
