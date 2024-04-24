import Products from './components/Products'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

const queryClientInstance = new QueryClient()

function App() {
  return (
    <>
      <QueryClientProvider client={queryClientInstance}>
        <Products />
      </QueryClientProvider >
    </>
  )
}

export default App
