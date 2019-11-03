import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { GET_EMAILDETAILS } from "./types";

export const getEmailDetails = () => (dispatch, getState) => {
  axios
    .post("/api/emailDetails/", tokenConfig(getState), {
      data: {
        address: "neilmichaelfranks@gmail.com",
        n: "5"
      }
    })
    .then(res => {
      dispatch({
        type: GET_EMAILDETAILS,
        payload: res.data.detailsList
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
