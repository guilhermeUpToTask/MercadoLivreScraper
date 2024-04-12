import { useQuery } from '@tanstack/react-query';
import { fetchAllProducts } from '../services/requests/ProductReq';
import { ProductType } from '../lib/types/types';

export default function useProductsQuery() {
    return useQuery<ProductType[]>({
        queryKey: ['products'],
        queryFn: fetchAllProducts,
    });
}
