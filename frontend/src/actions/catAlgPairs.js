import axios from "axios";
import { createMessage, returnErrors } from "./messages";
import { tokenConfig } from "./auth";

import { GET_CATALGPAIRS, DELETE_CATALGPAIR, ADD_CATALGPAIR } from "./types";

export const getCatAlgPairs = () => (dispatch, getState) => {
  axios
    .get("/api/catAlg/", tokenConfig(getState))
    .then(res => {
      dispatch({
        type: GET_CATALGPAIRS,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const deleteCatAlgPair = id => (dispatch, getState) => {
  axios
    .delete(`/api/catAlg/${id}/`, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ deleteCategory: "Category Deleted" }));
      dispatch({
        type: DELETE_CATALGPAIR,
        payload: id
      });
    })
    .catch(err => console.log(err));
};

export const addCatAlgPair = catAlgPair => (dispatch, getState) => {
  axios
    .post("/api/catAlg/", catAlgPair, tokenConfig(getState))
    .then(res => {
      dispatch(createMessage({ addCategory: "Category Added" }));
      dispatch({
        type: ADD_CATALGPAIR,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
