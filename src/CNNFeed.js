import React from 'react'
import feed from './scraper/CNNFeed.json'
import Card from 'react-bootstrap/Card'

class CNNFeed extends React.Component {
  render() {
    return (
      feed.map((feed) => (
        <Card style={{ width: '23rem' }} className="card">
          <Card.Body>
            <Card.Title className="cardTitle"> {feed.title} </Card.Title>     

            <Card.Text className="cardDescription"> {feed.description} </Card.Text>  

            <Card.Text> {feed.date} </Card.Text>    

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
                href="#header" 
                className="App-link" 
              >
                  Back to Top
              </a>
            </Card.Text>
          </Card.Body>
        </Card>
      ))
    )
  }
}

export default CNNFeed