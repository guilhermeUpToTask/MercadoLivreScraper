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
        <main className=' text-black mx-auto text-center bg-gray-200 '>
            <header className='bg-yellow-300 p-4 mb-8'>
                <h1 className='text-3xl font-bold font-sans'>Tracking Mercado Livre Product Prices - Ocultismo</h1>
            </header>
            <section className=''>
                <ProductList />
            </section>
        </main>
    )

}