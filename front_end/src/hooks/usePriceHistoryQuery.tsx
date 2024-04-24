import { useQuery } from '@tanstack/react-query';
import { fetchPriceHistory } from '../services/requests/PriceHisReq';
import { PriceHistoryType } from '../lib/types/types';

export default function usePriceHistoryQuery(product_id:number) {
    return useQuery<PriceHistoryType[]>({
        queryKey: ['price_history', product_id],
        queryFn:() => fetchPriceHistory(product_id),
    });
}
