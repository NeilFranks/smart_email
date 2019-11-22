import axios from "axios";
import { returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { ADD_CATEGORY, LOADING } from "./types";

export const createLabel = (label, emails) => (dispatch, getState) => {
  dispatch({
    type: LOADING,
    payload: true
  });
  axios
    .post("/api/createLabel/", tokenConfig(getState), {
      data: {
        label: label,
        emails: emails
      }
    })
    .then(res => {
      dispatch({
        type: ADD_CATEGORY,
        payload: res.data
      });

      dispatch({
        type: LOADING,
        payload: false
      });
      window.location.href = "/";
    })
    .catch(err => {
      dispatch(returnErrors(err.response.data, err.response.status));

      dispatch({
        type: LOADING,
        payload: false
      });
    });
};
