import React from "react";
import usePriceHistoryQuery from "../hooks/usePriceHistoryQuery";
import { AreaChart } from '@tremor/react';
import { PriceHistoryType } from "../lib/types/types";

interface IPriceHistoryProps {
    product_id: number;
}



const dataFormatter = (number: number) =>
    `$${Intl.NumberFormat('br').format(number).toString()}`;


export default function PriceHistory(props: IPriceHistoryProps): React.ReactElement {
    const { data: prices, error } = usePriceHistoryQuery(props.product_id);

    const pricesFormatter = (prices: PriceHistoryType[]) => {
        return prices.map((item: PriceHistoryType) => ({
            price: item.price,
            date: new Date(item.price_date).toLocaleDateString("en-US", { month: 'short', day: 'numeric' }),
        }));
    }

    if (error) return <p>Error fetching prices</p>;

    return (
        <section className="max-w-4xl mx-auto mt-2">
            {prices && <AreaChart
                className="h-80"
                data={pricesFormatter(prices)}
                index="date"
                categories={['price']}
                colors={['yellow']}
                valueFormatter={dataFormatter}
                yAxisWidth={60}
                onValueChange={(v) => console.log(v)}
            />}

        </section>
    );
}