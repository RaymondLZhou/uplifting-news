import React, { Component } from 'react';

import posts from './scraper/feed';
// get posts from online api
// it's return a json file
class GetLocalPosts extends Component {
    constructor(props){
        super(props);
        this.state = {            
            posts :posts            
        };
    }

    render() {
        const {posts} = this.state;
        return(
            <div>
                <ol className="item">
                {
                    posts.map(post => (
                        <li key={post.id} align="start">
                            <div>
                                <p className="title">{post.title}</p>
                            </div>
                        </li>
                    ))
                }
                </ol>
            </div>
        );
    }
  }
  
export default GetLocalPosts;
