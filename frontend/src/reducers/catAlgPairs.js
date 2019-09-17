// reducer: evaluate action and send down certain state depending on action
import { GET_CATALGPAIRS } from "../actions/types.js";

const initialState = {
  catAlgPairs: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_CATALGPAIRS:
      return {
        ...state,
        catAlgPairs: action.payload
      };
    default:
      return state;
  }
}
