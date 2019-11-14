import axios from "axios";
import { returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { GET_EMAILDETAILS, GET_CONNECTEDACCOUNTS } from "./types";

export const getEmailDetails = addressList => (dispatch, getState) => {
  axios
    .post("/api/emailDetails/", tokenConfig(getState), {
      data: {
        addressList: addressList,
        n: "15"
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

export const getConnectedAccounts = () => (dispatch, getState) => {
  axios
    .get("/api/connectedAddresses/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_CONNECTEDACCOUNTS,
        payload: res.data.addresses
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
