import { combineReducers } from "redux";
import users from "./users";
import catAlgPairs from "./catAlgPairs";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";

export default combineReducers({
  catAlgPairs,
  errors,
  messages,
  auth
});
