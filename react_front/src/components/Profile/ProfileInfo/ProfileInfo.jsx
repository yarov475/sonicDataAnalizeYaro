import React from "react";
import s from "./ProfileInfo.module.css"
import Preloader from "../../common/preloader/preloader";
const ProfileInfo = (props) => {
	if(!props.profile){
		return <Preloader/>
	}
	return (
		<div>
		<div >
			<img src="https://images.theconversation.com/files/223729/original/file-20180619-126566-1jxjod2.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1200&h=1200.0&fit=crop" height="300px" width="100%"></img>
			</div>
			<div className={s.descriptionBlock}>
				<img src={props.profile.photos.large}/>
			<p>{props.profile.aboutMe}</p>

				<p>{props.profile.contacts.facebook}</p>

				<p>{props.profile.lookingForAJob}</p>
				<p>{props.profile.lookingForAJobDescriptio}</p>

<p>{props.profile.fullName}</p>




			</div>
		</div >
	)
}
export default ProfileInfo;
