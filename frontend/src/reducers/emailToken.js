// reducer: evaluate action and send down certain state depending on action
import {
  GET_EMAILTOKEN,
  DELETE_EMAILTOKEN,
  ADD_EMAILTOKEN
} from "../actions/types.js";

const initialState = {
  emailToken: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_EMAILTOKEN:
      return {
        ...state,
        emailToken: action.payload
      };
    case DELETE_EMAILTOKEN:
      return {
        ...state,
        emailToken: state.emailToken.filter(
          emailToken => emailToken.id !== action.payload
        )
      };
    case ADD_EMAILTOKEN:
      return {
        ...state,
        emailToken: [...state.emailToken, action.payload]
      };
    default:
      return state;
  }
}
