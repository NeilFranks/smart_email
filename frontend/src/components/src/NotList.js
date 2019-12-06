import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTrainEmails, removeTrainEmails } from "../../actions/trainEmails";

export class NotList extends Component {
  static propTypes = {
    trainEmails: PropTypes.array.isRequired,
    getTrainEmails: PropTypes.func.isRequired,
    removeTrainEmails: PropTypes.func.isRequired
  };

  render() {
    return (
      <Fragment>
        <table className="table table-hover">
          <thead>
            <tr>
              <td>Emails not in category</td>
              <td> </td>
            </tr>
          </thead>
          <tbody>
            {this.props.trainEmails.map(trainEmails => (
              <tr key={trainEmails.id} bgcolor="#fff">
                <td
                  style={{
                    border: "none",
                    fontSize: "small",
                    width: "90%",
                    maxWidth: 0
                  }}
                >
                  <div>
                    <strong>{trainEmails.sender}</strong>
                  </div>
                  <div style={{ wordBreak: "break-word" }}>
                    <strong>{trainEmails.subject}</strong>
                    {snippetPrepend(trainEmails.snippet)}
                  </div>
                  <div>{dateString(new Date(trainEmails.date))}</div>
                </td>
                <td
                  style={{
                    border: "none",
                    width: "10%",
                    maxWidth: 0
                  }}
                  align="center"
                >
                  <button
                    onClick={() => this.props.removeTrainEmails(trainEmails)}
                    className="btn btn-success"
                  >
                    <strong>◄</strong>
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
  NotList
);
