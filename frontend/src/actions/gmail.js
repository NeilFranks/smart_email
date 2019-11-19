import axios from "axios";
import { returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { ADD_CATEGORY } from "./types";

export const createLabel = (label, emails) => (dispatch, getState) => {
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
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
