import React, { Component } from "react";

export class Categories extends Component {
  static propTypes = {
    category: PropTypes.array.isRequired,
    addCategory: PropTypes.func.isRequired,
    getCategory: PropTypes.func.isRequired,
    deleteCategory: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getCategory();
  }

  render() {
    return (
      <div>
        (
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
              {this.props.category.map(category => (
                <tr key={category.id}>
                  <td>{category.address}</td>
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
                <td />
                <td>
                  <button
                    onClick={this.props.addCategory.bind(this)}
                    className="btn btn-primary btn-sm"
                  >
                    {" "}
                    Add new account
                  </button>
                </td>
              </tr>
            </tfoot>
          </table>
        </Fragment>
        )
      </div>
    );
  }
}

const mapStateToProps = state => ({
  category: state.category.category // get reducer, then get its actual et
});

export default connect(
  mapStateToProps,
  { getCategory, deleteCategory, addCategory }
)(Category);
