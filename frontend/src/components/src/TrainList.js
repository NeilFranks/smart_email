import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTrainEmails, removeTrainEmails } from "../../actions/trainEmails";

export class TrainList extends Component {
  static propTypes = {
    trainEmails: PropTypes.array.isRequired,
    getTrainEmails: PropTypes.func.isRequired,
    removeTrainEmails: PropTypes.func.isRequired
  };

  render() {
    return (
      <Fragment>
        <table className="table">
          <tbody>
            {this.props.trainEmails.map(trainEmails => (
              <tr key={trainEmails.id} bgcolor="#fff">
                <td
                  style={{
                    whiteSpace: "nowrap",
                    overflow: "hidden",
                    textOverflow: "ellipsis",
                    width: "20%",
                    maxWidth: "0"
                  }}
                >
                  <strong>{trainEmails.sender}</strong>
                </td>
                <td
                  style={{
                    whiteSpace: "nowrap",
                    overflow: "hidden",
                    textOverflow: "ellipsis",
                    width: "65%",
                    maxWidth: "0"
                  }}
                >
                  <strong>{trainEmails.subject}</strong>
                  {snippetPrepend(trainEmails.snippet)}
                </td>
                <td
                  style={{
                    whiteSpace: "nowrap",
                    overflow: "hidden",
                    textOverflow: "ellipsis",
                    width: "15%",
                    maxWidth: "0"
                  }}
                  align="right"
                >
                  {dateString(new Date(trainEmails.date))}
                </td>
                <td>
                  <button
                    onClick={() => this.props.removeTrainEmails(trainEmails)}
                    className="btn btn-danger"
                  >
                    -
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  trainEmails: state.trainEmails.trainEmails // get reducer, then get its actual et
});

const dateString = someDate => {
  const today = new Date();
  const isToday =
    someDate.getDate() == today.getDate() &&
    someDate.getMonth() == today.getMonth() &&
    someDate.getFullYear() == today.getFullYear();

  const newDate = isToday
    ? someDate.toLocaleTimeString()
    : someDate.toLocaleDateString();

  return newDate;
};

const snippetPrepend = snippet => {
  return " - ".concat(snippet);
};

export default connect(mapStateToProps, { getTrainEmails, removeTrainEmails })(
  TrainList
);
