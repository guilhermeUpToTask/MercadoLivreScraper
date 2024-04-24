export type ProductType = {
    id: number;
    name: string;
    price: number;
    url: string;
    rating_amount: number;
    rating_number: number;
}

export type PriceHistoryType = {
    product_id: number
    price_date: string;
    price: number;
}