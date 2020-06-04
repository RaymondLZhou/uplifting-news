import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'
import GetLocalPosts from './displayFeed'

class App extends Component {
  render () {
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
            <button className="button">
             Link to Second Page
            </button>
          </Link>
  
          <GetLocalPosts/>
        </header>
      </div>
    )
  }
}

export default App
