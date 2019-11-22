// reducer: evaluate action and send down certain state depending on action
import {
  GET_TRAINIDS,
  ADD_TRAINIDS,
  REMOVE_TRAINIDS
} from "../actions/types.js";

const initialState = {
  trainIds: []
};

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_TRAINIDS:
      return {
        ...state,
        trainIds: action.payload
      };
    case REMOVE_TRAINIDS:
      return {
        ...state,
        trainIds: state.trainIds.filter(
          trainIds => trainIds.id !== action.payload
        )
      };
    case ADD_TRAINIDS:
      return {
        ...state,
        trainIds: [...state.trainIds, action.payload]
      };
    default:
      return state;
  }
}
