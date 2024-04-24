import React, { useState } from "react";
import PriceHistory from "./PriceHistory";

interface IProductProps {
    id: number;
    name: string;
    price: number;
    url: string;
    rating_amount: number;
    rating_number: number;

}

export default function Product(props: IProductProps): React.ReactElement {
    const [showPriceHistory, setShowPriceHistory] = useState(false);
    


    return (
        <article className="max-w-4xl mx-auto px-2 py-4 bg-white border border-b-0">
            <h2 className="text-sm font-bold mb-4"> {props.name} </h2>
            <section className="flex items-center justify-between">
                <span className="text-sm text-gray-600">Price: {props.price} </span>
                <p className="text-sm text-gray-600">Rating {props.rating_number} </p>
                <p className="text-sm text-gray-600">Rating Amount {props.rating_amount} </p>
                <a href={props.url} className="text-sm text-gray-500  hover:text-gray-200" target="_blank">
                    Product Page {'>'}
                </a>
            </section>
            <button
                className="text-sm text-gray-500  hover:text-gray-200 py-0 cursor-pointer"
                onClick={() =>setShowPriceHistory(!showPriceHistory)}>
                See Price History &#8595;
            </button>
            {showPriceHistory && <PriceHistory product_id={props.id} />}
        </article>
    )
}