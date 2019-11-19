import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  addCategory,
  getCategory,
  deleteCategory
} from "../../actions/categories";
import { getEmailDetails } from "../../actions/emailDetails";

export class Categories extends Component {
  static propTypes = {
    categories: PropTypes.array.isRequired,
    addCategory: PropTypes.func.isRequired,
    getCategory: PropTypes.func.isRequired,
    deleteCategory: PropTypes.func.isRequired,
    emailDetails: PropTypes.array.isRequired,
    getEmailDetails: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getCategory();
  }

  navToMakeCategory() {
    window.location.href = "makeCategory";
  }

  getEmailsFromLabel = label_id => {
    this.props.getEmailDetails(null, label_id);
  };

  render() {
    return (
      <div>
        <Fragment>
          <table className="table">
            <thead>
              <tr onClick={() => this.getEmailsFromLabel()}>
                <th style={{ fontWeight: "normal" }}>All Categories</th>
                {/* for deletion: */}
                <th />
              </tr>
            </thead>
            <tbody>
              {this.props.categories.map(category => (
                <tr
                  key={category.id}
                  onClick={() => this.getEmailsFromLabel(category.label_id)}
                >
                  <td>{category.name}</td>
                  <td>
                    <button
                      onClick={this.props.deleteCategory.bind(
                        this,
                        category.id
                      )}
                      className="btn btn-danger btn-sm"
                      style={{ width: "30px" }}
                    >
                      ✖
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
            <tfoot>
              <tr>
                <td>
                  <i>New Category</i>
                </td>
                <td>
                  <button
                    onClick={this.navToMakeCategory}
                    className="btn btn-primary btn-sm"
                    style={{ width: "30px" }}
                  >
                    <strong>＋</strong>
                  </button>
                </td>
              </tr>
            </tfoot>
          </table>
        </Fragment>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  categories: state.categories.categories,
  emailDetails: state.emailDetails.emailDetails
});

export default connect(mapStateToProps, {
  getCategory,
  deleteCategory,
  addCategory,
  getEmailDetails
})(Categories);
