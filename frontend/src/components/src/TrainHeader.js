import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTrainIds } from "../../actions/trainEmails";
import { createLabel } from "../../actions/gmail";

export class TrainHeader extends Component {
  state = {
    category: ""
  };

  static propTypes = {
    // trainModel: PropTypes.func.isRequired,
    trainIds: PropTypes.array.isRequired,
    trainEmails: PropTypes.array.isRequired,
    createLabel: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    this.props.createLabel(this.state.category, this.props.trainEmails);
  };

  render() {
    const { category } = this.state;
    return (
      <Fragment>
        <div className="card card-body mt-4 mb-4" style={{ border: "none" }}>
          <form onSubmit={this.onSubmit}>
            <div className="form-group" style={{ display: "inline-block" }}>
              <label
                style={{
                  display: "inline-block",
                  paddingRight: "10px",
                  fontSize: "large"
                }}
              >
                Category Name
              </label>
            </div>
            <div
              style={{
                display: "inline-block",
                paddingRight: "25px",
                width: "50%"
              }}
            >
              <input
                className="form-control"
                type="text"
                name="category"
                onChange={this.onChange}
                value={category}
              />
            </div>
            {arraySize(this.props.trainIds) === 1 ? (
              <div style={{ display: "inline-block" }}>
                <label
                  style={{
                    display: "inline-block",
                    paddingRight: "10px"
                  }}
                >
                  <i>{arraySize(this.props.trainIds)} email selected</i>
                </label>
              </div>
            ) : (
              <div style={{ display: "inline-block" }}>
                <label
                  style={{
                    display: "inline-block",
                    paddingRight: "10px"
                  }}
                >
                  <i>{arraySize(this.props.trainIds)} emails selected</i>
                </label>
              </div>
            )}
            <div
              className="form-group"
              style={{ display: "inline-block", float: "right" }}
            >
              <button type="submit" className="btn btn-success">
                Train
              </button>
            </div>
          </form>
        </div>
      </Fragment>
    );
  }
}

const arraySize = arr => {
  return arr.length;
};

const mapStateToProps = state => ({
  trainIds: state.trainIds.trainIds,
  trainEmails: state.trainEmails.trainEmails
});

export default connect(mapStateToProps, { getTrainIds, createLabel })(
  TrainHeader
);
