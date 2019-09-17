import axios from "axios";

import { GET_CATALGPAIRS } from "./types";

// GET CATEGORY ALGORITHM PAIRS
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
