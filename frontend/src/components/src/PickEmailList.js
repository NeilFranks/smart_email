import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getEmailDetails } from "../../actions/emailDetails";
import { addTrainEmails, getTrainIds } from "../../actions/trainEmails";

export class PickEmailList extends Component {
  static propTypes = {
    emailDetails: PropTypes.array.isRequired,
    getEmailDetails: PropTypes.func.isRequired,
    addTrainEmails: PropTypes.func.isRequired,
    trainIds: PropTypes.array.isRequired
  };

  componentDidMount() {
    this.props.getEmailDetails();
  }

  render() {
    return (
      <Fragment>
        <table className="table">
          <tbody>
            {this.props.emailDetails.map(emailDetails =>
              !containsObject(emailDetails.id, this.props.trainIds) ? (
                <tr key={emailDetails.id} bgcolor="#fff">
                  <td
                    style={{
                      width: "90%",
                      maxWidth: 0
                    }}
                  >
                    <table className="table">
                      <tr
                        style={{
                          fontSize: "small"
                        }}
                      >
                        <strong>{emailDetails.sender}</strong>
                      </tr>
                      <tr
                        style={{
                          fontSize: "small"
                        }}
                      >
                        <strong>{emailDetails.subject}</strong>
                        {snippetPrepend(emailDetails.snippet)}
                      </tr>
                      <tr
                        style={{
                          fontSize: "small"
                        }}
                      >
                        {dateString(new Date(emailDetails.date))}
                      </tr>
                    </table>
                  </td>
                  <td
                    style={{
                      width: "10%",
                      maxWidth: 0
                    }}
                    align="center"
                  >
                    <button
                      onClick={() =>
                        this.props.addTrainEmails({ emailDetails })
                      }
                      className="btn btn-info"
                    >
                      +
                    </button>
                  </td>
                </tr>
              ) : null
            )}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

function containsObject(obj, list) {
  var i;
  for (i = 0; i < list.length; i++) {
    if (list[i].id === obj) {
      return true;
    }
  }

  return false;
}

const mapStateToProps = state => ({
  emailDetails: state.emailDetails.emailDetails, // get reducer, then get its actual et
  trainIds: state.trainIds.trainIds
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

export default connect(mapStateToProps, {
  getEmailDetails,
  addTrainEmails,
  getTrainIds
})(PickEmailList);
