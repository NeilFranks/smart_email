import axios from "axios";
import { createMessage } from "./messages";

import {
  GET_CATALGPAIRS,
  DELETE_CATALGPAIR,
  ADD_CATALGPAIR,
  GET_ERRORS
} from "./types";

export const getCatAlgPairs = () => dispatch => {
  axios
    .get("/api/catAlg/")
    .then(res => {
      dispatch({
        type: GET_CATALGPAIRS,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};

export const deleteCatAlgPair = id => dispatch => {
  axios
    .delete(`/api/catAlg/${id}/`)
    .then(res => {
      dispatch(createMessage({ deleteCategory: "Category Deleted" }));
      dispatch({
        type: DELETE_CATALGPAIR,
        payload: id
      });
    })
    .catch(err => console.log(err));
};

export const addCatAlgPair = catAlgPair => dispatch => {
  axios
    .post("/api/catAlg/", catAlgPair)
    .then(res => {
      dispatch(createMessage({ addCategory: "Category Added" }));
      dispatch({
        type: ADD_CATALGPAIR,
        payload: res.data
      });
    })
    .catch(err => {
      const errors = {
        msg: err.response.data,
        status: err.response.status
      };
      dispatch({
        type: GET_ERRORS,
        payload: errors
      });
    });
};
