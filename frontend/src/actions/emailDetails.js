import axios from "axios";
import { returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import {
  GET_EMAILDETAILS,
  ADD_EMAILDETAILS,
  GET_CONNECTEDACCOUNTS,
  SET_SELECTEDLABEL
} from "./types";

export const getEmailDetails = (before_time, label_id) => (
  dispatch,
  getState
) => {
  if (before_time == null) {
    before_time = Math.floor(Date.now() / 1000);
  }
  axios
    .post("/api/emailDetails/", tokenConfig(getState), {
      data: {
        n: "15",
        before_time: before_time,
        label_id: label_id
      }
    })
    .then(res => {
      dispatch({
        type: SET_SELECTEDLABEL,
        payload: label_id
      });
      dispatch({
        type: GET_EMAILDETAILS,
        payload: res.data.detailsList
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const addEmailDetails = before_time => (dispatch, getState) => {
  if (before_time == null) {
    before_time = Math.floor(Date.now() / 1000);
  }
  axios
    .post("/api/emailDetails/", tokenConfig(getState), {
      data: {
        n: "15",
        before_time: before_time
      }
    })
    .then(res => {
      dispatch({
        type: ADD_EMAILDETAILS,
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
