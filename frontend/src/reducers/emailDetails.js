// reducer: evaluate action and send down certain state depending on action
import { GET_EMAILDETAILS, GET_CONNECTEDACCOUNTS,GET_EMAIL } from "../actions/types.js";

const initialState = {
  emailDetails: [],
  connectedAccounts: [],
  email: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_EMAILDETAILS:
      return {
        ...state,
        emailDetails: action.payload
      };
    
    case GET_EMAIL:
      return{
        ...state,
        email: action.payload
      };
    case GET_CONNECTEDACCOUNTS:
      return {
        ...state,
        connectedAccounts: action.payload
      };
    default:
      return state;
  }
}
