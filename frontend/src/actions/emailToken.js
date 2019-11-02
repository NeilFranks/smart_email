import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { GET_EMAILTOKEN, DELETE_EMAILTOKEN, ADD_EMAILTOKEN } from "./types";

export const newEmailToken = () => (dispatch, getState) => {
  axios
    .get("/api/connectNewEmail/", tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ addEmail: "Added " }));
      dispatch({
        type: ADD_EMAILTOKEN,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const getEmailToken = () => (dispatch, getState) => {
  axios
    .get("/api/et/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_EMAILTOKEN,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const deleteEmailToken = id => (dispatch, getState) => {
  axios
    .delete(`/api/et/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ deleteEmail: "Email Address Deleted" }));
      dispatch({
        type: DELETE_EMAILTOKEN,
        payload: id
      });
    })
    .catch(err => console.log(err));
};
