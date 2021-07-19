import React from "react";
import s from  './../Dialog.module.css';
import {NavLink} from "react-router-dom";

const Dialogitem = (props)=> {
    let path = "/dialogs/"+props.id;

    return <div className={s.dialog + ' ' + s.active} >
        <img src ={props.src}  />
        <NavLink to={path} >  {props.name} </NavLink>

    </div>
}


export default Dialogitem;