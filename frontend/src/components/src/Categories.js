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
    getEmailDetails: PropTypes.func.isRequired,
    selectedLabel: PropTypes.object
  };

  componentDidMount() {
    this.props.getCategory();
  }

  navToMakeCategory() {
    window.location.href = "makeCategory";
  }

  getEmailsFromLabel = category => {
    this.props.getEmailDetails(null, category);
  };

  render() {
    return (
      <div>
        <Fragment>
          <table className="table table-hover">
            <tbody>
              {this.props.selectedLabel == null ? (
                <tr onClick={() => this.getEmailsFromLabel()} bgcolor="#eee">
                  {/* TODO: needs to just get from inbox by default, instead of all including sent */}
                  <td>Inbox</td>
                  {/* for deletion: */}
                  <td />
                </tr>
              ) : (
                <tr onClick={() => this.getEmailsFromLabel()}>
                  <td style={{ fontWeight: "normal" }}>Inbox</td>
                  {/* for deletion: */}
                  <td />
                </tr>
              )}
              {this.props.categories.map(category =>
                this.props.selectedLabel != null &&
                this.props.selectedLabel.name == category.name ? (
                  <tr
                    key={category.id}
                    onClick={() => this.getEmailsFromLabel(category)}
                    bgcolor="#eee"
                  >
                    <td>
                      <strong>{category.name}</strong>
                    </td>
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
                ) : (
                  <tr
                    key={category.id}
                    onClick={() => this.getEmailsFromLabel(category)}
                  >
                    {this.highlight ? (
                      <td bgcolor="#f00">{category.name}</td>
                    ) : (
                      <td>{category.name}</td>
                    )}
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
                )
              )}
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
  emailDetails: state.emailDetails.emailDetails,
  selectedLabel: state.emailDetails.selectedLabel
});

export default connect(mapStateToProps, {
  getCategory,
  deleteCategory,
  addCategory,
  getEmailDetails
})(Categories);
