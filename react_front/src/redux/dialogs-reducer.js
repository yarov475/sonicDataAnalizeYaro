const UPDATE_NEW_MESSAGE_BODY = 'UPDATE_NEW_MESSAGE_BODY';
const SEND_MESSAGE = 'SEND_MESSAGE';


let initialState = {
    dialogs: [
        {
            id: 1,
            name: 'Dima',
            src: "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMWFhUXFxUVFxcYFxoYFxUYFRUWFxUVFxcYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGhAQGy0lICUtL"
        },
        {id: 2, name: 'Sacha'}
    ],

    messages: [
        {id: 1, message: "hi, guy!!!!!"},
        {id: 2, message: "Coool"}
    ],
    newMessageBody: " "
};
const dialogsReducer = (state = initialState, action) => {
    let stateCopy;
    switch (action.type) {
        case UPDATE_NEW_MESSAGE_BODY:
                return {...state,
                newMessageBody: action.body
                            };

        case SEND_MESSAGE:
            let body= state.newMessageBody
            return {
                ...state,
                newMessageBody: ' ',
                messages: [...state.messages, {id: 6, message: body}]
            };

        default:
            return state;

    }

}

export const sendMessageCreator = () => ({type: SEND_MESSAGE})
export const updateNewMessageBodyCreator = (body) =>
    ({type: UPDATE_NEW_MESSAGE_BODY, body: body})


export default dialogsReducer;


