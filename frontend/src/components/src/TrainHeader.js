import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTrainIds } from "../../actions/trainEmails";
import { createLabel } from "../../actions/gmail";
import Loader from "../layout/Loader";

export class TrainHeader extends Component {
  state = {
    category: ""
  };

  static propTypes = {
    // trainModel: PropTypes.func.isRequired,
    trainIds: PropTypes.array.isRequired,
    trainEmails: PropTypes.array.isRequired,
    createLabel: PropTypes.func.isRequired,
    loading: PropTypes.bool
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    if (this.state.category && this.props.trainEmails.length > 0) {
      this.props.createLabel(this.state.category, this.props.trainEmails);
      this.render();
    }
    //TODO: else
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
            {this.props.loading ? (
              <div
                style={{
                  display: "inline-block"
                }}
              >
                <Loader
                  style={{ position: "fixed", marginTop: "-35px" }}
                ></Loader>
              </div>
            ) : (
              <div
                style={{
                  display: "inline-block"
                }}
              ></div>
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
  trainEmails: state.trainEmails.trainEmails,
  loading: state.categories.loading
});

export default connect(mapStateToProps, { getTrainIds, createLabel })(
  TrainHeader
);
