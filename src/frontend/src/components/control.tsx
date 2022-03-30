import React from 'react'
import { useNavigate } from 'react-router-dom'


interface GoBackProps {
    className?: string,
    children?: React.ElementType | string
}


export function GoBack(props: GoBackProps){
    const navigate = useNavigate()

    let className: string = 'link-like '
    if(props.className)
        className += props.className

    return <button className={className} onClick={() => navigate(-1)}>
        {props.children ?? 'back'}
    </button>
}
