import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addEmailPass } from "../../actions/emailPass";

export class Form extends Component {
  state = {
    email: "",
    appPass: ""
  };

  static propTypes = {
    addEmailPass: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    const { email, appPass } = this.state;
    const emailPass = { email, appPass };
    this.props.addEmailPass(emailPass);
    this.setState({
      email: "",
      appPass: ""
    });
  };

  render() {
    const { email, appPass } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Connect an Email Address</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Email Address</label>
            <input
              className="form-control"
              type="text"
              name="email"
              onChange={this.onChange}
              value={email}
            />
          </div>
          <div className="form-group">
            <label>App Password</label>
            <input
              className="form-control"
              type="text"
              name="appPass"
              onChange={this.onChange}
              value={appPass}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(
  null,
  { addEmailPass }
)(Form);
