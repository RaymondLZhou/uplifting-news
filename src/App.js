import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'
import CardColumns from 'react-bootstrap/CardColumns'
import FeedDisplay from './FeedDisplay.js'

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo"/>
          <p> Uplifting News </p>

          <Link to="/second-page">
            <button className="button" id="spaces">
            Link to Second Page
            </button>
          </Link>

          <a className="App-link" href="#body"> See News </a>
        </header>

        <body className="App-body" id="body">
          <CardColumns className="cardColumns"> <FeedDisplay/> </CardColumns>
        </body>
      </div>
    )
  }
}

export default App
