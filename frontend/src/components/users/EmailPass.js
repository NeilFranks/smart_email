import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getEmailPass, deleteEmailPass } from "../../actions/emailPass";

export class EmailPass extends Component {
  static propTypes = {
    emailPass: PropTypes.array.isRequired,
    getEmailPass: PropTypes.func.isRequired,
    deleteEmailPass: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getEmailPass();
  }

  render() {
    return (
      <Fragment>
        <h2>Emails and Passwords</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Email</th>
              <th>Password</th>
              {/* for deletion: */}
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.emailPass.map(emailPass => (
              <tr key={emailPass.id}>
                <td>{emailPass.email}</td>
                <td>{emailPass.appPass}</td>
                <td>
                  <button
                    onClick={this.props.deleteEmailPass.bind(
                      this,
                      emailPass.id
                    )}
                    className="btn btn-danger btn-sm"
                  >
                    {" "}
                    Delete
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
  emailPass: state.emailPass.emailPass // get reducer, then get its actual emailPass
});

export default connect(
  mapStateToProps,
  { getEmailPass, deleteEmailPass }
)(EmailPass);
