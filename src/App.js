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
            href="/#" 
            className="App-link" 
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
        <img src={logo} className="App-logo" alt="logo"/>
        <p>
          Uplifting News
        </p>

        <Link to="/second-page">
          <button className="button" id="spaces">
           Link to Second Page
          </button>
        </Link>

        <a
          className="App-link"
          href="#body"
        >
          See News
        </a>
      </header>

        <body className="App-body" id="body">
          <CardColumns className="cardColumn"> {display} </CardColumns>
        </body>

    </div>
  )
}

export default App
