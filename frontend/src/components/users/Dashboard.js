import React, { Fragment } from "react";
import Form from "./Form";
import CatAlgPairs from "./CatAlgPairs";

export default function Dashboard() {
  const policy = (
    <ul className="navbar-nav ml-auto mt-2 mt-lg-0">
      <li className="nav-item">
        <a href="/privacy-policy">Privacy Policy</a>
      </li>
    </ul>
  );

  return (
    <Fragment>
      <Form />
      <CatAlgPairs />
      <div>{policy}</div>
    </Fragment>
  );
}
