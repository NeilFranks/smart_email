import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getEmailToken, deleteEmailToken } from "../../actions/emailToken";

export class EmailToken extends Component {
  static propTypes = {
    emailToken: PropTypes.array.isRequired,
    getEmailToken: PropTypes.func.isRequired,
    deleteEmailToken: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getEmailToken();
  }

  render() {
    return (
      <Fragment>
        <h2>Connected Email Addresses</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Email Address</th>

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
  { getEmailToken, deleteEmailToken }
)(EmailToken);
