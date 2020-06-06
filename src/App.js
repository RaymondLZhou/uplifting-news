import React from 'react'
import { Link } from 'react-router-dom'
import logo from './logo.svg'
import './App.css'

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo"/>
          <p> Uplifting News </p>

          <div className="links">
            <Link to="/bbc-news" className="link">
              <button className="button" id="spaces">
              Link to BBC News
              </button>
            </Link>

            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

            <Link to="/cnn-news">
              <button className="button" id="spaces">
              Link to CNN News
              </button>
            </Link>
          </div>

          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    )
  }
}

export default App
