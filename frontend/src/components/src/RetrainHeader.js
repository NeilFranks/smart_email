import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTrainIds } from "../../actions/trainEmails";
import { retrainLabel } from "../../actions/gmail";
import { getCategory } from "../../actions/categories";
import { getEmailDetails } from "../../actions/emailDetails";

import Loader from "../layout/Loader";

export class RetrainHeader extends Component {
  static propTypes = {
    categories: PropTypes.array.isRequired,
    getCategory: PropTypes.func.isRequired,
    trainIds: PropTypes.array.isRequired,
    trainEmails: PropTypes.array.isRequired,
    retrainLabel: PropTypes.func.isRequired,
    loading: PropTypes.bool
  };

  componentDidMount() {
    this.props.getCategory();
  }

  onChange = e => {
    const categoryID = e.target.value;
    var category = null;
    for (var i = 0; i < this.props.categories.length; i++) {
      if ((this.props.categories[i].id = categoryID)) {
        category = this.props.categories[i];
      }
    }

    this.props.getEmailDetails(null, category);
  };

  onSubmit = e => {
    e.preventDefault();
    if (this.state.category && this.props.trainEmails.length > 0) {
      this.props.retrainLabel(this.state.category, this.props.trainEmails);
      this.render();
    }
    //TODO: else
  };

  categorySelect() {
    return (
      <select
        className="custom-select"
        name="category"
        onChange={this.onChange}
      >
        <option defaultValue="">Open this select menu</option>
        {this.props.categories.map(category => (
          <option key={category.id} value={category.id}>
            {category.name}
          </option>
        ))}
      </select>
    );
  }

  render() {
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
              {this.categorySelect()}
            </div>

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
                Retrain
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
  categories: state.categories.categories,
  trainIds: state.trainIds.trainIds,
  trainEmails: state.trainEmails.trainEmails,
  loading: state.categories.loading
});

export default connect(mapStateToProps, {
  getCategory,
  getTrainIds,
  retrainLabel,
  getEmailDetails
})(RetrainHeader);
