import { GET_TRAINEMAILS, REMOVE_TRAINEMAILS, ADD_TRAINEMAILS } from "./types";

export const addTrainEmails = email => dispatch => {
  dispatch({
    type: ADD_TRAINEMAILS,
    payload: {
      id: email.emailDetails.id,
      sender: email.emailDetails.sender,
      subject: email.emailDetails.subject,
      snippet: email.emailDetails.snippet,
      date: email.emailDetails.date
    }
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
