// reducer: evaluate action and send down certain state depending on action
import {
  ADD_CATEGORY,
  GET_CATEGORY,
  DELETE_CATEGORY
} from "../actions/types.js";

const initialState = {
  categories: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_CATEGORY:
      return {
        ...state,
        categories: action.payload
      };
    case ADD_CATEGORY:
      return {
        ...state,
        categories: [...state.categories, action.payload]
      };
    case DELETE_CATEGORY:
      return {
        ...state,
        categories: state.categories.filter(
          categories => categories.id !== action.payload
        )
      };
    default:
      return state;
  }
}
