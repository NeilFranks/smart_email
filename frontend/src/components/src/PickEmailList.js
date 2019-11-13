import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getEmailDetails } from "../../actions/emailDetails";
import { addTrainEmails } from "../../actions/trainEmails";

export class PickEmailList extends Component {
  static propTypes = {
    emailDetails: PropTypes.array.isRequired,
    getEmailDetails: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getEmailDetails();
  }

  render() {
    return (
      <Fragment>
        <table className="table">
          <tbody>
            {this.props.emailDetails.map(emailDetails => (
              <tr key={emailDetails.id} bgcolor="#fff">
                <td
                  style={{
                    whiteSpace: "nowrap",
                    overflow: "hidden",
                    textOverflow: "ellipsis",
                    width: "20%",
                    maxWidth: "0"
                  }}
                >
                  <strong>{emailDetails.sender}</strong>
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
                  <strong>{emailDetails.subject}</strong>
                  {snippetPrepend(emailDetails.snippet)}
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
                  {dateString(new Date(emailDetails.date))}
                </td>
                <td>
                  <button
                    onClick={addTrainEmails(emailDetails)}
                    className="btn btn-info"
                  >
                    +
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
  emailDetails: state.emailDetails.emailDetails // get reducer, then get its actual et
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

export default connect(
  mapStateToProps,
  { getEmailDetails }
)(PickEmailList);
