import axios from "axios";

import { GET_CATALGPAIRS, DELETE_CATALGPAIR, ADD_CATALGPAIR } from "./types";

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
      dispatch({
        type: ADD_CATALGPAIR,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};
