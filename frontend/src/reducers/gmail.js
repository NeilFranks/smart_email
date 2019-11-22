// reducer: evaluate action and send down certain state depending on action
import { CREATE_LABEL } from "../actions/types.js";

export default function(state = initialState, action) {
  switch (action.type) {
    case CREATE_LABEL:
      return {
        ...state,
        categories: action.payload
      };
    default:
      return;
  }
}
