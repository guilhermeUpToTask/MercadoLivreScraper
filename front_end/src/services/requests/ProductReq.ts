import axiosInstance from "../instances/axiosInstance";
import type { ProductType } from "../../lib/types/types";



export async function fetchAllProducts(): Promise<ProductType[]> {
    try {
        const { data, status, } = await axiosInstance.get('/products')
        if (status !== 200) throw new Error('Error While Fetching all Products, status:'+status);
        
        return data as ProductType[];

    } catch (e) {
        console.error('Error Fetching all Products, ' + e);
        throw e
    }
}