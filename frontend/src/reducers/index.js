import { combineReducers } from "redux";
import users from "./users";
import emailPass from "./emailPass";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";

export default combineReducers({
  emailPass,
  errors,
  messages,
  auth
});
