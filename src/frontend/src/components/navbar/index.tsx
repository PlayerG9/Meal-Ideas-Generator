import './index.css'
import { Link } from 'react-router-dom'
import User from '../../user_control'


export default function Navbar(){
    return <div className='navbar'>
        <img className='icon' src={null} alt=""/>
        <NavMenu/>
    </div>
}


function NavMenu(){
    return <div className='navmenu'>
        <Link to="/user/me">
            User
        </Link>
        <Link to="/">
            Home
        </Link>
        <Link to="/about">
            About
        </Link>
    </div>
}
