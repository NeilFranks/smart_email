import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getEmailDetails } from "../../actions/emailDetails";

export class EmailList extends Component {
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
        <table className="table table-striped">
          <tbody>
            {this.props.emailDetails.map(emailDetails => (
              <tr key={emailDetails.id}>
                <td>{emailDetails.sender}</td>
                <td>{emailDetails.subject}</td>
                <td>{emailDetails.date}</td>
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

export default connect(
  mapStateToProps,
  { getEmailDetails }
)(EmailList);
