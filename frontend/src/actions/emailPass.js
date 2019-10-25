import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { GET_EMAILPASS, DELETE_EMAILPASS, ADD_EMAILPASS } from "./types";

export const getEmailPass = () => (dispatch, getState) => {
  axios
    .get("/api/ep/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_EMAILPASS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const deleteEmailPass = id => (dispatch, getState) => {
  axios
    .delete(`/api/ep/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ deleteEmail: "Email Address Deleted" }));
      dispatch({
        type: DELETE_EMAILPASS,
        payload: id
      });
    })
    .catch(err => console.log(err));
};

export const addEmailPass = EmailPass => (dispatch, getState) => {
  axios
    .post("/api/ep/", EmailPass, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ addEmail: "Email Address Added" }));
      dispatch({
        type: ADD_EMAILPASS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
