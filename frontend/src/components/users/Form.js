import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { newEmailToken } from "../../actions/emailToken";

export class Form extends Component {
  state = {
    address: ""
  };

  static propTypes = {
    newEmailToken: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    const { address } = this.state;
    const emailToken = { address };
    this.props.newEmailToken(emailToken);
    this.setState({
      creds: "",
      address: ""
    });
  };

  render() {
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Connect a new GMail account</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Connect
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(
  null,
  { newEmailToken }
)(Form);
