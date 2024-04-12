import React from "react";


interface IProductProps {
    id: number;
    name: string;
    price: number;
    url: string;
    rating_amount: number;
    rating_number: number;

}

export default function Product(props: IProductProps) : React.ReactElement{
    return (
        <ul>
            <li>Product {props.name} </li>
            <li>Price {props.price} </li>
            <li>Url {props.url} </li>
            <li>Rating {props.rating_number} </li>
            <li>Rating Amount {props.rating_amount} </li>
        </ul>
    )
}