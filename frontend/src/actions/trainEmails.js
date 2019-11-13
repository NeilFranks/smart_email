import axios from "axios";
import { GET_TRAINEMAILS, REMOVE_TRAINEMAILS, ADD_TRAINEMAILS } from "./types";

export const addTrainEmails = email => (dispatch, getState) => {
  console.log(email.id);
  axios.dispatch({
    type: ADD_TRAINEMAILS,
    payload: email
  });
};

export const getTrainEmails = () => (dispatch, getState) => {
  dispatch({
    type: GET_TRAINEMAILS,
    payload: getState
  });
};

export const removeTrainEmails = id => dispatch => {
  dispatch({
    type: REMOVE_TRAINEMAILS,
    payload: id
  });
};
