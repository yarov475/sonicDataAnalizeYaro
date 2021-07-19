import React from "react";
import s from "./Post.module.css"
const Post = (props) => {
	return (
		<div>
			<div className={s.item}>
				<img src="https://sun9-56.userapi.com/c855436/v855436374/2442e1/IAPoU3LXuYI.jpg" alt="" />
				{props.message}
				<div className={s.like}>
					<span>  Like </span>{props.LikesCount}
				</div>
			</div>
		</div>
	);
}
export default Post;