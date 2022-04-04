import { ReactChild } from "react";
import { UserInterface } from ".";


interface UserIconProps {
    user: UserInterface,
    className?: string,
    children: ReactChild
}

// <svg xmlns='http://www.w3.org/2000/svg' version='1.1' height='50px' width='120px'><text x='0' y='15' fill='gray' font-size='20'>🗑</text></svg>

export default function UserIcon(props: UserIconProps){
    const iconText = props.user.username.slice(0,2)
    const svgText = `<text x='0' y='0' fill='gray' font-size='20'>${iconText}</text>`
    const svgData = `<svg xmlns='http://www.w3.org/2000/svg' version='1.1' height='50px' width='50px'>${svgText}</svg>`
    const imageSrc = `${svgData}`
    return <img className={props.className} src={imageSrc}>
        {props.children}
    </img>
}
