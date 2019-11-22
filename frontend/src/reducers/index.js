import { combineReducers } from "redux";
import categories from "./category";
import emailToken from "./emailToken";
import emailDetails from "./emailDetails";
import errors from "./errors";
import messages from "./messages";
import trainEmails from "./trainEmails";
import trainIds from "./trainIds";
import auth from "./auth";

export default combineReducers({
  categories,
  emailDetails,
  emailToken,
  errors,
  messages,
  trainEmails,
  trainIds,
  auth
});
