import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getEmailDetails, addEmailDetails } from "../../actions/emailDetails";
import { addTrainEmails, getTrainIds } from "../../actions/trainEmails";

export class CategoryList extends Component {
  static propTypes = {
    emailDetails: PropTypes.array.isRequired,
    getEmailDetails: PropTypes.func.isRequired,
    addEmailDetails: PropTypes.func.isRequired,
    addTrainEmails: PropTypes.func.isRequired,
    trainIds: PropTypes.array.isRequired
  };

  componentDidMount() {}

  render() {
    return (
      <Fragment>
        <table className="table table-hover">
          <thead>
            <tr>
              <td>Emails in category</td>
              <td> </td>
            </tr>
          </thead>
          <tbody>
            {this.props.emailDetails.map(emailDetails =>
              !containsObject(emailDetails.id, this.props.trainIds) ? (
                <tr key={emailDetails.id} bgcolor="#fff">
                  <td
                    style={{
                      border: "none",
                      fontSize: "small",
                      width: "90%",
                      maxWidth: 0
                    }}
                  >
                    <div>
                      <strong>{emailDetails.sender}</strong>
                    </div>
                    <div style={{ wordBreak: "break-word" }}>
                      <strong>{emailDetails.subject}</strong>
                      {snippetPrepend(emailDetails.snippet)}
                    </div>
                    <div>{dateString(new Date(emailDetails.date))}</div>
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
                      onClick={() =>
                        this.props.addTrainEmails({ emailDetails })
                      }
                      className="btn btn-info"
                    >
                      <strong>+</strong>
                    </button>
                  </td>
                </tr>
              ) : null
            )}
          </tbody>
          <tfoot>
            <tr>
              <td>
                <button
                  onClick={() => this.loadMore(this.props.emailDetails)}
                  className="btn btn-info"
                >
                  Load More
                </button>
              </td>
              <td />
            </tr>
          </tfoot>
        </table>
      </Fragment>
    );
  }

  loadMore(emails) {
    const last_email = emails[emails.length - 1];
    const last_date = last_email.date;
    const last_date_epoch = dateEpoch(new Date(last_date));
    this.props.addEmailDetails(last_date_epoch);
    this.render();
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

const dateEpoch = someDate => {
  return someDate.getTime() / 1000;
};

const snippetPrepend = snippet => {
  return " - ".concat(snippet);
};

export default connect(mapStateToProps, {
  getEmailDetails,
  addEmailDetails,
  addTrainEmails,
  getTrainIds
})(CategoryList);
