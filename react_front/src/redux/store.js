import profileReducer from "./profile-reducer";
import dialogsReducer from "./dialogs-reducer";
import sidebarReducer from "./sidebar-reducer";


let store = {
    _state: {
        profilePage: {
            newPostText:"Whattt?!",
            posts: [
                {id: 1, message: "how are you?", likesCount: 12},
                {id: 2, message: "helo Friend!!!", likesCount: 15},
                {id: 3, message: "helo Friends!!!", likesCount: 15}
            ]
        },
        dialogPage: {
            dialogs: [
                {id: 1, name: 'Dima', src:"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMWFhUXFxUVFxcYFxoYFxUYFRUWFxUVFxcYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGhAQGy0lICUtL"},
                {id: 2, name: 'Sacha'}
            ],

            messages:[
                {id: 1, message: "hi, guy!!!!!"},
                {id: 2, message: "Coool"}
            ],
            newMessageBody: " "
        },
        sideBar: {
        },

    },
    subscribe(observer) {
        this._callSubscriber=observer;
    },
    getState() {
        return this._state;
    },
    _callSubscriber() {
        console.log('state changed');
    },


   dispatch(action) {
this._state.profilePage =  profileReducer(this._state.profilePage,action);
this._state.dialogPage =  dialogsReducer(this._state.dialogPage,action);
this._state.sideBar =  sidebarReducer(this._state.sideBar,action);

this._callSubscriber(this._state);


   }
}
export default store;
window.store =store;