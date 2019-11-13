import React, { Fragment } from "react";
import EmailList from "./EmailList";
import Categories from "./Categories";

export default function ViewEmailDashboard() {
  return (
    <Fragment>
      <table className="table">
        <tbody>
          <tr>
            <td
              style={{
                whiteSpace: "nowrap",
                overflow: "hidden",
                textOverflow: "ellipsis",
                width: "20%",
                maxWidth: "0"
              }}
            >
              <Categories />
            </td>

            <td
              style={{
                whiteSpace: "nowrap",
                overflow: "hidden",
                textOverflow: "ellipsis",
                width: "80%",
                maxWidth: "0"
              }}
            >
              <EmailList />
            </td>
          </tr>
        </tbody>
      </table>
    </Fragment>
  );
}
