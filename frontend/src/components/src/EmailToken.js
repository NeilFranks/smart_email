import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  addEmailToken,
  getEmailToken,
  deleteEmailToken
} from "../../actions/emailToken";

export class EmailToken extends Component {
  static propTypes = {
    emailToken: PropTypes.array.isRequired,
    addEmailToken: PropTypes.func.isRequired,
    getEmailToken: PropTypes.func.isRequired,
    deleteEmailToken: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getEmailToken();
  }

  render() {
    return (
      <Fragment>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Connected Accounts</th>
              {/* for deletion: */}
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.emailToken.map(emailToken => (
              <tr key={emailToken.id}>
                <td>{emailToken.address}</td>
                <td>
                  <button
                    onClick={this.props.deleteEmailToken.bind(
                      this,
                      emailToken.id
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
          <tfoot>
            <tr>
              <td />
              <td>
                <button
                  onClick={this.props.addEmailToken.bind(this)}
                  className="btn btn-primary btn-sm"
                >
                  {" "}
                  Add new account
                </button>
              </td>
            </tr>
          </tfoot>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  emailToken: state.emailToken.emailToken // get reducer, then get its actual et
});

export default connect(
  mapStateToProps,
  { getEmailToken, deleteEmailToken, addEmailToken }
)(EmailToken);
