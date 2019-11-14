// reducer: evaluate action and send down certain state depending on action
import {
  GET_EMAILDETAILS,
  GET_CONNECTEDACCOUNTS,
  HIDE_EMAIL,
  UNHIDE_EMAIL
} from "../actions/types.js";

const initialState = {
  emailDetails: [],
  connectedAccounts: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_EMAILDETAILS:
      return {
        ...state,
        emailDetails: action.payload
      };
    case GET_CONNECTEDACCOUNTS:
      return {
        ...state,
        connectedAccounts: action.payload
      };
    case HIDE_EMAIL:
      return {
        ...state,
        emailDetails: state.emailDetails.filter(
          emailDetails => emailDetails.id !== action.payload
        )
      };
    case UNHIDE_EMAIL:
      return {
        ...state,
        emailDetails: [...state.emailDetails, action.payload]
      };
    default:
      return state;
  }
}
