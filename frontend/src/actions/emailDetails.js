import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { GET_EMAILDETAILS } from "./types";
import emailDetails from "../reducers/emailDetails";

export const getEmailDetails = () => (dispatch, getState) => {
  axios
    .post("/api/emailDetails/", tokenConfig(getState), {
      data: {
        address: "neilmichaelfranks@gmail.com",
        n: "10"
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
