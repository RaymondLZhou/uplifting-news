import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'
import CardColumns from 'react-bootstrap/CardColumns'
import BBCFeed from './BBCFeed.js'

class SecondPage extends React.Component {
  render () {
    return (
      <div className="App">
        <header className="App-header" id="header">
          <img src={logo} className="App-logo" alt="logo" />
          <p> BBC News </p>
          
          <Link to="/">
            <button className="button" id="spaces">
             Link to First Page
            </button>
          </Link>

          <a className="App-link" href="#body"> See News </a>
        </header>

        <body className="App-body" id="body">
          <CardColumns className="cardColumns"> <BBCFeed/> </CardColumns>
        </body>
      </div>
    );
  }
}

export default SecondPage
