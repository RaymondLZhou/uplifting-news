import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'
import CardColumns from 'react-bootstrap/CardColumns'
import Feed1 from './Feed1.js'

class Sentiment extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header" id="header">
          <img src={logo} className="App-logo" alt="logo" />
          <p> Uplifting News </p>
          
          <Link to="/">
            <button className="button">
             See sentiment
            </button>
          </Link>

          <a className="App-link" href="#body" id="spaces"> See News </a>
        </header>

        <body className="App-body" id="body">
          <CardColumns className="cardColumns"> <Feed1/> </CardColumns>
        </body>
      </div>
    );
  }
}

export default Sentiment
