import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'
import CardColumns from 'react-bootstrap/CardColumns'
import Feed from './Feed.js'

class Sentiment extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header" id="header">
          <img src={logo} className="App-logo" alt="logo" />
          <p> Uplifting News </p>
          
          <Link to="/">
            <button className="button">
             Link to First Page
            </button>
          </Link>

          <a className="App-link" href="#body" id="spaces"> See News </a>
        </header>

        <body className="App-body" id="body">
          <CardColumns className="cardColumns"> <Feed/> </CardColumns>
        </body>
      </div>
    );
  }
}

export default Sentiment
