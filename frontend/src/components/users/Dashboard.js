import React, { Fragment } from "react";
import Form from "./Form";
import Users from "./Users";
import CatAlgPairs from "./CatAlgPairs";

export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <CatAlgPairs />
    </Fragment>
  );
}
