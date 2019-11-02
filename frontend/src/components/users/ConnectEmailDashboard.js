import React, { Fragment } from "react";
import Form from "./Form";
import EmailToken from "./EmailToken";

export default function ConnectEmailDashboard() {
  return (
    <Fragment>
      <Form />
      <EmailToken />
    </Fragment>
  );
}
