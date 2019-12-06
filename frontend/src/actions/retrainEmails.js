import {
  GET_RETRAINEMAILS,
  REMOVE_RETRAINEMAILS,
  ADD_RETRAINEMAILS,
  ADD_RETRAINIDS,
  REMOVE_RETRAINIDS,
  GET_RETRAINIDS
} from "./types";

export const addRetrainEmails = email => dispatch => {
  dispatch({
    type: ADD_RETRAINEMAILS,
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
    type: ADD_RETRAINIDS,
    payload: { id: email.emailDetails.id }
  });
};

export const getRetrainEmails = () => (dispatch, getState) => {
  dispatch({
    type: GET_RETRAINEMAILS,
    payload: getState
  });
};

export const removeRetrainEmails = email => dispatch => {
  dispatch({
    type: REMOVE_RETRAINEMAILS,
    payload: email.id
  });

  dispatch({
    type: REMOVE_RETRAINIDS,
    payload: email.id
  });
};

export const getRetrainIds = () => (dispatch, getState) => {
  dispatch({
    type: GET_RETRAINIDS,
    payload: getState
  });
};
