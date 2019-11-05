import { combineReducers } from "redux";
import emailToken from "./emailToken";
import emailDetails from "./emailDetails";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";

export default combineReducers({
  emailDetails,
  emailToken,
  errors,
  messages,
  auth
});
