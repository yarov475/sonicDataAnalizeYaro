import React from "react";
import {addPostActionCreator, updateNewPostTextActionCreeator} from "../../../redux/profile-reducer"
import MyPosts from "./MyPosts";

// import mapStateToProps from "react-redux/lib/connect/mapStateToProps";
// import mapDispatchToProps from "react-redux/lib/connect/mapDispatchToProps";
import {connect} from "react-redux";


// const MyPostsContainer = (props) =>
// {
//     return (
//         <StoreContext.Consumer>
//             {
//                 (store) => {
//                     let state = store.getState();
//                     let addpost = () => {
//                         //props.addPost();
//                         store.dispatch(addPostActionCreator());
//                     }
//
//                     let onPostChange = (text) => {
//                         let action = updateNewPostTextActionCreeator(text);
//                         store.dispatch(action);
//                     }
//                     return <MyPosts updateNewPostText={onPostChange}
//                                     addPost={addpost}
//                                     posts={state.profilePage.posts}
//                                     newPostText={state.profilePage.newPostText}/>
//
//                 }
//             }
//         </StoreContext.Consumer>
//
//     )
// }
const mapStateToProps=(state)=>{
    return{
        posts:state.profilePage.posts,
        newPostText:state.profilePage.newPostText
    }
}
  const mapDispatchToProps=(dispatch)=>{
    return{
        updateNewPostText:(text)=>{
            let action=updateNewPostTextActionCreeator(text);
            dispatch(action);
        },
        addPost:()=>{
            dispatch(addPostActionCreator());
        }
    }
}


const MyPostsContainer = connect(mapStateToProps, mapDispatchToProps)(MyPosts);
export default MyPostsContainer;