import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addCatAlgPair } from "../../actions/catAlgPairs";

export class Form extends Component {
  state = {
    category: "",
    emails: [],
    common_words: [],
  };

  static propTypes = {
    addCatAlgPair: PropTypes.func.isRequired
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    const { category, emails, common_words } = this.state;
    const catAlgPair = { category, emails, common_words };
    this.props.addCatAlgPair(catAlgPair);
    this.setState({
      category: "",
      emails: [],
      common_words: []
    });
  };

  render() {
    const { category, emails, common_words } = this.state;
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
            <label>Emails</label>
            <input
              className="form-control"
              type="text"
              name="emails"
              onChange={this.onChange}
              value={emails}
            />
          </div>
          <div className="form-group">
            <label>Most Common Words</label>
            <input
              className="form-control"
              type="text"
              name="common_words"
              onChange={this.onChange}
              value={common_words}
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
