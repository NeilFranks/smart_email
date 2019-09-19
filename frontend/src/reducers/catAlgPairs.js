// reducer: evaluate action and send down certain state depending on action
import {
  GET_CATALGPAIRS,
  DELETE_CATALGPAIR,
  ADD_CATALGPAIR
} from "../actions/types.js";

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
    case DELETE_CATALGPAIR:
      return {
        ...state,
        catAlgPairs: state.catAlgPairs.filter(
          catAlgPair => catAlgPair.id !== action.payload
        )
      };
    case ADD_CATALGPAIR:
      return {
        ...state,
        catAlgPairs: [...state.catAlgPairs, action.payload]
      };
    default:
      return state;
  }
}
