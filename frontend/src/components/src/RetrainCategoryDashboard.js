import React, { Fragment } from "react";
import RetrainHeader from "./RetrainHeader";
import CategoryList from "./CategoryList";
import NotList from "./NotList";

export default function RetrainCategoryDashboard() {
  return (
    <Fragment>
      <RetrainHeader />
      <table className="table">
        <tbody>
          <tr>
            <td
              style={{
                width: "50%",
                maxWidth: "0",
                overflow: "scroll"
              }}
            >
              <CategoryList />
            </td>

            <td
              style={{
                width: "50%",
                maxWidth: "0",
                overflow: "scroll"
              }}
            >
              <NotList />
            </td>
          </tr>
        </tbody>
      </table>
    </Fragment>
  );
}
