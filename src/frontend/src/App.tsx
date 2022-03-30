import './App.css'
import './generell.css'
import {
    QueryClientProvider
} from 'react-query'
import { queryClient } from './apicall'
import Router from './routes'


export default function App() {
    return <>
        <QueryClientProvider client={queryClient}>
            <Router/>
        </QueryClientProvider>
    </>
}
