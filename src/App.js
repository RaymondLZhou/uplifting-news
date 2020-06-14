import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'
import CardColumns from 'react-bootstrap/CardColumns'
import Feed from './Feed.js'

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo"/>
          <p> Uplifting News </p>

          <Link to="/sentiment">
            <button className="button" id="spaces">
             Link to Second Page
            </button>
          </Link>

          <a className="App-link" href="#body" id="spaces"> See News </a>
        </header>

        <body className="App-body" id="body">
          <CardColumns className="cardColumns"> <Feed/> </CardColumns>
        </body>
      </div>
    )
  }
}

export default App
