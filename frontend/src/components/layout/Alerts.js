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
      console.log(error);
      if (error.msg.detail) {
        const message = error.status + ": " + error.msg.detail;
        alert.error(message);
      } else if (error.msg.category) {
        alert.error("Category: " + error.msg.category.join());
      } else if (error.msg.algorithm) {
        alert.error("todo: algorithm shouldn't be an input field. whoops");
      } else if (error.status == 409) {
        alert.error("A category with that name already exists");
      } else {
        alert.error("Error");
      }
    }

    if (message !== prevProps.message) {
      console.message;
      if (message.deleteCategory) alert.success(message.deleteCategory);
      if (message.addCategory) alert.success(message.addCategory);
      if (message.decide)
        alert.success(message.decide + " emails added to categories");
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
