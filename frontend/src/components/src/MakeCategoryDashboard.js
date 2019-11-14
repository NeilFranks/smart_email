import React, { Fragment } from "react";
import TrainHeader from "./TrainHeader";
import PickEmailList from "./PickEmailList";
import TrainList from "./TrainList";

export default function ViewEmailDashboard() {
  return (
    <Fragment>
      <TrainHeader />
      <table className="table">
        <tbody>
          <tr>
            <td
              style={{
                width: "50%",
                maxWidth: "0"
              }}
            >
              <PickEmailList />
            </td>

            <td
              style={{
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
