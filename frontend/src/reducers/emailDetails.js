// reducer: evaluate action and send down certain state depending on action
import { GET_EMAILDETAILS } from "../actions/types.js";

const initialState = {
  emailDetails: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_EMAILDETAILS:
      return {
        ...state,
        emailDetails: action.payload
      };
    default:
      return state;
  }
}
