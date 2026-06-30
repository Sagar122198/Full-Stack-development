import React from 'react';
class Item extends React.Component{
    constructor(props){
        super(props)
        this.state={
            click:0
        }
    }
    clicked() {
        this.setState({
            click:this.state.click+1

        })
        console.log(`this ${this.props.fruit} was clicked.`,this.state.click)
        
    }
    render(){
        return( 
            <div>

                <h1 onClick={ ()=>this.clicked() }>hello {this.props.fruit}</h1> 
                <p>{this.state.click} no of times clicked</p>
            </div>
        );
    }
}
export default Item;