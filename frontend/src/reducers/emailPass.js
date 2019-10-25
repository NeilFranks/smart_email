// reducer: evaluate action and send down certain state depending on action
import {
  GET_EMAILPASS,
  DELETE_EMAILPASS,
  ADD_EMAILPASS
} from "../actions/types.js";

const initialState = {
  emailPass: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_EMAILPASS:
      return {
        ...state,
        emailPass: action.payload
      };
    case DELETE_EMAILPASS:
      return {
        ...state,
        emailPass: state.emailPass.filter(
          emailPass => emailPass.id !== action.payload
        )
      };
    case ADD_EMAILPASS:
      return {
        ...state,
        emailPass: [...state.emailPass, action.payload]
      };
    default:
      return state;
  }
}
