import { useState } from "react";
import Hero from "./Hero";
import { useParams } from "react-router-dom";
import { useEffect } from "react";

const movieView = () => {
    const {id} = useParams()

    const [movieDetails , setMovieDetails] = useState({})
    useEffect= ()=>{
        
    }
    return (
        <Hero/>
    )
}
export default movieView;