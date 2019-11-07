// reducer: evaluate action and send down certain state depending on action
import { GET_EMAILDETAILS, GET_CONNECTEDACCOUNTS } from "../actions/types.js";

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
    default:
      return state;
  }
}
