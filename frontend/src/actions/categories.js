import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import {
  GET_CATEGORY,
  DELETE_CATEGORY,
  ADD_CATEGORY,
  GET_EMAILDETAILS,
  SET_SELECTEDLABEL
} from "./types";

export const addCategory = () => (dispatch, getState) => {
  axios
    .post("/api/category/", tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ addCategory: "Added " }));
      dispatch({
        type: ADD_CATEGORY,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const getCategory = () => (dispatch, getState) => {
  axios
    .get("/api/category/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_CATEGORY,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const deleteCategory = id => (dispatch, getState) => {
  axios
    .delete(`/api/category/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch({
        type: SET_SELECTEDLABEL,
        payload: null
      });
      dispatch(createMessage({ deleteCategory: "Category Deleted" }));
      dispatch({
        type: DELETE_CATEGORY,
        payload: id
      });
    })
    .catch(err => console.log(err));

  //get inbox emails

  const before_time = Math.floor(Date.now() / 1000);
  axios
    .post("/api/emailDetails/", tokenConfig(getState), {
      data: {
        n: "15",
        before_time: before_time,
        label_id: null
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
