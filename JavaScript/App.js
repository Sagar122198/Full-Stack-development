// import logo from './logo.svg';
import './App.css';
// import Item from "./item";
import React from 'react';

class FilmByRow extends React.Component {
  render() {
    return (
      <li>
        <a href={this.props.url} > {this.props.url}</a>
      </li>
    )
  }
}

class StarWars extends React.Component {
  constructor() {
    super()

    this.state = {
      load: false,
      name: null,
      height: null,
      HomeWorld: null,
      films: []
    }
  }
  getRandomCharater() {
    let RandomNumber = Math.floor(Math.random() * 82);
    const url = `https://swapi.info/api/people/${RandomNumber}/`;
    fetch(url)
      .then(response => response.json())
      .then(data => {
        // console.log(data);
        this.setState({
          name: data.name,
          height: data.height,
          HomeWorld: data.homeworld,
          films: data.films,
          load: true
        })
      })
  }
  render() {
    const movies = this.state.films.map((url, i) => {
      return <FilmByRow key={i} url={url} />
    })
    return (
      <div>
        {
          this.state.load &&
          <div>
            <h1>{this.state.name}</h1>
            <p>{this.state.height} in cm</p>
            <p><a href={this.state.HomeWorld} >Homeworld</a></p>
            <ul> {movies} </ul>
          </div>
        }
        <button type="button" onClick={() => this.getRandomCharater()} className='btn'>Random Character 🚀</button>
      </div>
    )
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <StarWars />
      </header>
    </div>
  );
}
export default App;
