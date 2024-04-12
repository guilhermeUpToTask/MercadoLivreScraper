import React from 'react';
import Product from './Product';
import useProductsQuery from '../hooks/useProductsQuery';

export default function Products(): React.ReactElement {
    const { data: products, error } = useProductsQuery();

    const ProductList = () => {
        if (error) return <p>Error: {error.message}</p>

        if (!products) return <p>Loading...</p>

        return products.map((product) => {
            return <Product key={product.id} id={product.id} name={product.name} price={product.price} url={product.url} rating_amount={product.rating_amount} rating_number={product.rating_number} />
        })
    }

    return (
        <section>
            <h1>Products List - Mercado Livre - Ocultismo</h1>
            <ProductList />
        </section>
    )

}