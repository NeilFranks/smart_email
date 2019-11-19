import {
  GET_TRAINEMAILS,
  REMOVE_TRAINEMAILS,
  ADD_TRAINEMAILS,
  ADD_TRAINIDS,
  REMOVE_TRAINIDS,
  GET_TRAINIDS
} from "./types";

export const addTrainEmails = email => dispatch => {
  dispatch({
    type: ADD_TRAINEMAILS,
    payload: {
      address: email.emailDetails.address,
      id: email.emailDetails.id,
      sender: email.emailDetails.sender,
      subject: email.emailDetails.subject,
      snippet: email.emailDetails.snippet,
      date: email.emailDetails.date
    }
  });

  dispatch({
    type: ADD_TRAINIDS,
    payload: { id: email.emailDetails.id }
  });
};

export const getTrainEmails = () => (dispatch, getState) => {
  dispatch({
    type: GET_TRAINEMAILS,
    payload: getState
  });
};

export const removeTrainEmails = email => dispatch => {
  dispatch({
    type: REMOVE_TRAINEMAILS,
    payload: email.id
  });

  dispatch({
    type: REMOVE_TRAINIDS,
    payload: email.id
  });
};

export const getTrainIds = () => (dispatch, getState) => {
  dispatch({
    type: GET_TRAINIDS,
    payload: getState
  });
};
