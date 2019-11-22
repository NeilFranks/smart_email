import React, { Fragment } from "react";
import EmailList from "./EmailList";
import Categories from "./Categories";

export default function ViewEmailDashboard() {
  return (
    <Fragment>
      <div style={{ overflow: "hidden" }}>
        <div style={{ float: "left", width: "200px" }}>
          <Categories />
        </div>
        <div style={{ overflow: "hidden", paddingLeft: "5px" }}>
          <EmailList />
        </div>
      </div>
    </Fragment>
  );
}
