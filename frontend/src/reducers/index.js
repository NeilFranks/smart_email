import { combineReducers } from "redux";
import users from "./users";
import emailToken from "./emailToken";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";

export default combineReducers({
  emailToken,
  errors,
  messages,
  auth
});
