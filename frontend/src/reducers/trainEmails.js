// reducer: evaluate action and send down certain state depending on action
import {
  GET_TRAINEMAILS,
  ADD_TRAINEMAILS,
  REMOVE_TRAINEMAILS
} from "../actions/types.js";

const initialState = {
  trainEmails: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_TRAINEMAILS:
      return {
        ...state,
        trainEmails: action.payload
      };
    case REMOVE_TRAINEMAILS:
      return {
        ...state,
        trainEmails: state.trainEmails.filter(
          trainEmails => trainEmails.id !== action.payload
        )
      };
    case ADD_TRAINEMAILS:
      var i;
      for (i = 0; i < state.trainEmails.length; i++) {
        if (state.trainEmails[i].id === action.payload.id) {
          // return existing state if email is already in list
          return {
            ...state,
            trainEmails: [...state.trainEmails]
          };
        }
      }

      // add email if it wasn't already in list
      return {
        ...state,
        trainEmails: [...state.trainEmails, action.payload]
      };
    default:
      return state;
  }
}
