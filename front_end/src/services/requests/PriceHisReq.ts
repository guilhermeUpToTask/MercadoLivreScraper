import axiosInstance from "../instances/axiosInstance";
import { PriceHistoryType } from "../../lib/types/types";


export async function fetchPriceHistory(product_id:number): Promise<PriceHistoryType[]> {
    try {
        const { data, status, } = await axiosInstance.get(`/products/${product_id}/price_history`)
        if (status !== 200) throw new Error('Error While Fetching price history, status:'+status);
        
        return data as PriceHistoryType[];

    } catch (e) {
        console.error('Error Fetching all Products, ' + e);
        throw e
    }
}