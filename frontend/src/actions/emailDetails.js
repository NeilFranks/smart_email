import axios from "axios";
import { returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { GET_EMAILDETAILS, GET_CONNECTEDACCOUNTS, GET_EMAIL } from "./types";
import emailDetails from "../reducers/emailDetails";
import {
  GET_EMAILDETAILS,
  ADD_EMAILDETAILS,
  GET_CONNECTEDACCOUNTS,
  SET_SELECTEDLABEL
} from "./types";

export const getEmailDetails = (before_time, category) => (
  dispatch,
  getState
) => {
  // set the label you selected
  dispatch({
    type: SET_SELECTEDLABEL,
    payload: category
  });

  // if a before_time was not specified, make it the current time
  if (before_time == null) {
    before_time = Math.floor(Date.now() / 1000);
  }

  // if a category was specified, extract the values from it
  var label_id = null;
  if (category != null) {
    label_id = category.label_id;
  }

  //get the emails from any specified category, before the specified time
  axios
    .post("/api/emailDetails/", tokenConfig(getState), {
      data: {
        n: "15",
        before_time: before_time,
        label_id: label_id
      }
    })
    .then(res => {
      //return the list of emails obtained
      dispatch({
        type: GET_EMAILDETAILS,
        payload: res.data.detailsList
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const getEmail = (EMAIL) => (dispatch, getState) => {

    dispatch({
      type: GET_EMAIL,
      payload: EMAIL
    });
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

export const decide = emails => (dispatch, getState) => {
  console.log(emails);
  axios
    .post("/api/setPageLabel/", tokenConfig(getState), {
      data: {
        emails: emails
      }
    })
    .then(res => {
      dispatch(createMessage({ decide: "Sorted some emails" }));
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
