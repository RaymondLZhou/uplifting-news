import React from 'react'
import logo from './logo.svg'
import './App.css'
import CardColumns from 'react-bootstrap/CardColumns'
import Feed from './Feed.js'

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <header className="App-header" id="header">
          <img src={logo} className="App-logo" alt="logo"/>

          <p className="title"> Uplifting News </p>
          <p> See the most positive news first </p>

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
