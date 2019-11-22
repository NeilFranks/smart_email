import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getEmailDetails, decide } from "../../actions/emailDetails";
import Loader from "../layout/Loader";

export class EmailList extends Component {
  page_times = [];

  static propTypes = {
    emailDetails: PropTypes.array.isRequired,
    getEmailDetails: PropTypes.func.isRequired,
    selectedLabel: PropTypes.object,
    loading: PropTypes.bool,
    decide: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getEmailDetails();
  }

  render() {
    return (
      <Fragment>
        <button
          className="btn btn-success"
          onClick={() => this.prev()}
          style={{ fontSize: "small" }}
        >
          newer
        </button>
        <button
          style={{ marginLeft: "200px", fontSize: "small" }}
          className="btn btn-info"
          onClick={() => this.props.decide(this.props.emailDetails)}
        >
          DECIDE
        </button>
        <button
          style={{ float: "right", fontSize: "small" }}
          className="btn btn-success"
          onClick={() => this.next(this.props.emailDetails)}
        >
          older
        </button>
        {!this.props.loading ? (
          !this.props.emailDetails.length ? (
            <div
              style={{
                color: "#555555",
                position: "fixed",
                top: "30%",
                left: "50%"
              }}
            >
              no emails found
            </div>
          ) : (
            <table
              className="table table-hover"
              style={{ fontSize: "smaller" }}
            >
              <tbody>
                {this.props.emailDetails.map(emailDetails =>
                  emailDetails.unread ? (
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
                    </tr>
                  ) : (
                    <tr key={emailDetails.id} bgcolor="#ddd">
                      <td
                        style={{
                          whiteSpace: "nowrap",
                          overflow: "hidden",
                          textOverflow: "ellipsis",
                          width: "20%",
                          maxWidth: "0"
                        }}
                      >
                        {emailDetails.sender}
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
                        {emailDetails.subject}
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
                    </tr>
                  )
                )}
              </tbody>
            </table>
          )
        ) : (
          <Loader
            style={{
              position: "fixed",
              top: "30%",
              left: "50%"
            }}
          />
        )}
      </Fragment>
    );
  }

  prev() {
    const prev_page_timestamp = this.page_times.pop();
    this.props.getEmailDetails(prev_page_timestamp, this.props.selectedLabel);
    this.render();
  }

  next(emails) {
    // first, save off most recent email time stamp so you can page back to this page later
    const first_email = emails[0];
    const first_date = first_email.date;
    const first_date_epoch = dateEpoch(new Date(first_date));
    this.page_times.push(first_date_epoch + 60);

    // now, load next set of emails
    const last_email = emails[emails.length - 1];
    const last_date = last_email.date;
    const last_date_epoch = dateEpoch(new Date(last_date));
    this.props.getEmailDetails(last_date_epoch, this.props.selectedLabel);
    this.render();
  }
}

const mapStateToProps = state => ({
  emailDetails: state.emailDetails.emailDetails,
  selectedLabel: state.emailDetails.selectedLabel,
  loading: state.emailDetails.loading
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
  decide
})(EmailList);
