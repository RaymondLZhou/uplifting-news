import React from 'react'
import feed from './data/displayFeed.json'
import Card from 'react-bootstrap/Card'

class Feed extends React.Component {
  render() {
    return (
      feed.map((feed) => (
        <Card style={{ width: '23rem' }} className="card">
          <Card.Body>
            <Card.Title className="cardTitle"> {feed.title} </Card.Title>      

            <div className="cardBody">
            <Card.Text className="cardOverallScore"> Overall Score: {feed.overall} </Card.Text> 
            <Card.Text> Positive Score: {feed.positive} </Card.Text> 
            <Card.Text> Neutral Score: {feed.neutral} </Card.Text> 
            <Card.Text className="cardNegativeScore"> Negative Score: {feed.negative} </Card.Text> 
            </div>

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

export default Feed
