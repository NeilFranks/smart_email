import React, { Component, Fragment } from "react";
import { withAlert } from "react-alert";
import { connect } from "react-redux";
import PropTypes from "prop-types";

export class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired
  };

  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;
    if (error !== prevProps.error) {
      if (error.msg.detail) {
        const message = error.status + ": " + error.msg.detail;
        alert.error(message);
      } else {
        alert.error("error that idk how to handle..");
      }
    }

    if (message !== prevProps.message) {
      if (message.deleteCategory) alert.success(message.deleteCategory);
      if (message.addCategory) alert.success(message.addCategory);
    }
  }

  render() {
    return <Fragment />;
  }
}

const mapStateToProps = state => ({
  error: state.errors,
  message: state.messages
});

export default connect(mapStateToProps)(withAlert()(Alerts));
