import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";

export class TrainHeader extends Component {
  state = {
    category: ""
  };

  static propTypes = {
    // trainModel: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    // this.props.trainModel(category);
  };

  render() {
    const { category } = this.state;
    return (
      <Fragment>
        <div className="card card-body mt-4 mb-4">
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Category Name</label>
              <input
                className="form-control"
                type="text"
                name="category"
                onChange={this.onChange}
                value={category}
              />
            </div>
            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Train
              </button>
            </div>
          </form>
        </div>
      </Fragment>
    );
  }
}

export default connect(null, {})(TrainHeader);
