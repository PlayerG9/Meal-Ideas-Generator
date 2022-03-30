import './index.css'
import { Link } from 'react-router-dom'
import { GoBack } from '../../components/control'


export default function PageNotFound(){
    return <div className='page-not-found'>
        <h1>404 Page Not Found</h1>
        <div className='options'>
            <Link to="/">🏠 Home</Link>
            <GoBack>↩ Last Page</GoBack>
        </div>
    </div>
}
