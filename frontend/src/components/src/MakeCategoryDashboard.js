import React, { Fragment } from "react";
import PickEmailList from "./PickEmailList";
import TrainList from "./TrainList";

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
                width: "50%",
                maxWidth: "0"
              }}
            >
              <PickEmailList />
            </td>

            <td
              style={{
                whiteSpace: "nowrap",
                overflow: "hidden",
                textOverflow: "ellipsis",
                width: "50%",
                maxWidth: "0"
              }}
            >
              <TrainList />
            </td>
          </tr>
        </tbody>
      </table>
    </Fragment>
  );
}
