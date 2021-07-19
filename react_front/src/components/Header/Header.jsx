import React from "react";
import s from "./Header.module.css";
import {NavLink} from "react-router-dom";

const Header = (props) => {
	return (
		<header className={s.header}>
			<img src="https://author.today/content/2019/08/12/16d805b54b8e446da8718f51a6208727.jpg?width=750&height=500&mode=min" ></img>

			<div className={s.loginBlock}>
				{ props.isAuth? props.login
					: <NavLink to= {'/login'}>Login </NavLink>
								}
			</div>


			<div className={s.item}>FRIENDS CORE</div>
		</header>

	);

}
export default Header;