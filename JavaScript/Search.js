import Hero from "./Hero";
const MovieTitle = ({ movie }) => {
    const posterUrl = `https://image.tmdb.org/t/p/w500/${movie.poster_path}`
    return (
        <div className="col-lg-3 col-md-3 col-2 my-4">
            <div className="card" >
                <img src={posterUrl} className="card-img-top" alt={movie.original_title} />
                <div className="card-body">
                    <h5 className="card-title">{movie.original_title}</h5>
                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    <a href="#" className="btn btn-primary">Go somewhere</a>
                </div>
            </div>
        </div>
    )
}

const Search = ({ keyword, searchResults }) => {
    const title = `You are searching ${keyword}`
    const resultHtml = searchResults.map((obj, i) => {
        return <MovieTitle movie={obj} key={i} />
    })
    return (<div>
        <Hero text={title} />
        {resultHtml &&
            <div className="container">
                <div className="row">
                    {resultHtml}
                </div>
            </div>
        }
    </div>)
}
export default Search;

// 2c6e45683a00f902377abe10f42b95bc

// https://api. themoviedb.org/3/search/movie?api_key=2c6e45683a00f902377abe10f42b95bc&language=en-US&query=star%20wars&page=1&include_adult=false
