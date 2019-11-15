import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import {
  addCategory,
  getCategory,
  deleteCategory
} from "../../actions/categories";

export class Categories extends Component {
  static propTypes = {
    categories: PropTypes.array.isRequired,
    addCategory: PropTypes.func.isRequired,
    getCategory: PropTypes.func.isRequired,
    deleteCategory: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getCategory();
  }

  navToMakeCategory() {
    console.log("gagae");
    window.location.href = "makeCategory";
  }

  render() {
    return (
      <div>
        <Fragment>
          <table className="table">
            <thead>
              <tr>
                <th>Categories</th>
                {/* for deletion: */}
                <th />
              </tr>
            </thead>
            <tbody>
              {this.props.categories.map(category => (
                <tr key={category.id}>
                  <td>{category.name}</td>
                  <td>
                    <button
                      onClick={this.props.deleteCategory.bind(
                        this,
                        category.id
                      )}
                      className="btn btn-danger btn-sm"
                    >
                      {" "}
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
            <tfoot>
              <tr>
                <td
                  style={{
                    whiteSpace: "nowrap",
                    overflow: "hidden",
                    textOverflow: "ellipsis",
                    width: "80%",
                    maxWidth: "0"
                  }}
                >
                  <i>New Category</i>
                </td>
                <td
                  align="right"
                  style={{
                    whiteSpace: "nowrap",
                    width: "20%",
                    maxWidth: "0"
                  }}
                >
                  <button
                    onClick={this.navToMakeCategory}
                    className="btn btn-primary btn-sm"
                  >
                    +
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
  categories: state.categories.categories // get reducer, then get its actual et
});

export default connect(mapStateToProps, {
  getCategory,
  deleteCategory,
  addCategory
})(Categories);
