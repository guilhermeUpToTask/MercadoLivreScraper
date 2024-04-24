import React from "react";
import usePriceHistoryQuery from "../hooks/usePriceHistoryQuery";

interface IPriceHistoryProps {
    product_id: number;
}

export default function PriceHistory(props: IPriceHistoryProps): React.ReactElement {
    const { data: prices, error } = usePriceHistoryQuery(props.product_id);

    const PriceList = () => {
        if (error) return <p>Error: {error.message}</p>

        if (!prices) return <p>Loading...</p>

        return prices.map((price) => {
            return <p key={price.price_date}>price: {price.price} date: {price.price_date}</p>
        })
    }
    
    return (
        <section className="max-w-4xl mx-auto mt-2">
            <PriceList/>
        </section>
    )
}