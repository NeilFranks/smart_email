// reducer: evaluate action and send down certain state depending on action
import {
  GET_EMAILDETAILS,
  ADD_EMAILDETAILS,
  GET_CONNECTEDACCOUNTS,
  SET_SELECTEDLABEL
} from "../actions/types.js";

const initialState = {
  selectedLabel: null,
  emailDetails: [],
  connectedAccounts: [],
  loading: false
};

export default function(state = initialState, action) {
  switch (action.type) {
    case ADD_EMAILDETAILS:
      var emails = [...state.emailDetails];
      action.payload.map(email => emails.push(email));

      return {
        ...state,
        emailDetails: emails
      };
    case GET_EMAILDETAILS:
      return {
        ...state,
        emailDetails: action.payload,
        loading: false
      };
    case SET_SELECTEDLABEL:
      return {
        ...state,
        selectedLabel: action.payload,
        emailDetails: [],
        loading: true
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
