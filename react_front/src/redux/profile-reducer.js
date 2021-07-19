import {usersApi} from "../API/api";

const ADD_POST = 'ADD-POST';
const UPDATE_NEW_POST_TEXT = 'UPDATE-NEW-POST-TEXT';
const SET_USER_PROFILE = 'SET-SER-PROFILE';

let initialState = {
    newPostText: "Whattt?!",
    posts: [
        {id: 1, message: "how are you?", likesCount: 12},
        {id: 2, message: "helo Friend!!!", likesCount: 15},
        {id: 3, message: "helo Friends!!!", likesCount: 15}
    ],
    profile: null
};


const profileReducer = (state = initialState, action) => {
    switch (action.type) {
        case ADD_POST: {
            let newPost = {
                id: 5,
                message: state.newPostText,
                likesCount: 1
            };
            return {
                ...state,
                posts: [...state.posts, newPost],
                newPostText: ''
            };


        }
        case UPDATE_NEW_POST_TEXT: {
            return {
                ...state,
                newPostText: action.newText
            }
        }
        case SET_USER_PROFILE:{
            return {...state,profile: action.profile}
        }
        default:
            return state;
    }
}
export const addPostActionCreator = () => ({type: ADD_POST})
export const setUserProfile=(profile)=>({type: SET_USER_PROFILE, profile})

export const getUserProfile=(userId)=>(dispatch)=>{
    usersApi.getProfile(userId).then(response => {
        dispatch(setUserProfile(response.data));
    });
}


export const updateNewPostTextActionCreeator = (text) =>
    ({type: UPDATE_NEW_POST_TEXT, newText: text})

export default profileReducer;
