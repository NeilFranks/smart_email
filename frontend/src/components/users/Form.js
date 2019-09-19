import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addCatAlgPair } from "../../actions/catAlgPairs";

export class Form extends Component {
  state = {
    category: "",
    algorithm: ""
  };

  static propTypes = {
    addCatAlgPair: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    const { category, algorithm } = this.state;
    const catAlgPair = { category, algorithm };
    this.props.addCatAlgPair(catAlgPair);
    this.setState({
      category: "",
      algorithm: ""
    });
  };

  render() {
    const { category, algorithm } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add Category</h2>
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
            <label>Algorithm</label>
            <input
              className="form-control"
              type="text"
              name="algorithm"
              onChange={this.onChange}
              value={algorithm}
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
  { addCatAlgPair }
)(Form);
