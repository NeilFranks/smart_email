import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getCatAlgPairs, deleteCatAlgPair } from "../../actions/catAlgPairs";

export class CatAlgPairs extends Component {
  static propTypes = {
    catAlgPairs: PropTypes.array.isRequired,
    getCatAlgPairs: PropTypes.func.isRequired,
    deleteCatAlgPair: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getCatAlgPairs();
  }

  render() {
    return (
      <Fragment>
        <h2>Categories and Algorithms</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Category</th>
              <th>Emails</th>
              <th>Common Words</th>
              {/* for deletion: */}
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.catAlgPairs.map(catAlgPair => (
              <tr key={catAlgPair.id}>
                <td>{catAlgPair.category}</td>
                <td>{catAlgPair.emails}</td>
                <td>{catAlgPair.common_words}</td>
                <td>
                  <button
                    onClick={this.props.deleteCatAlgPair.bind(
                      this,
                      catAlgPair.id
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
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  catAlgPairs: state.catAlgPairs.catAlgPairs // get reducer, then get its actual catAlgPairs
});

export default connect(
  mapStateToProps,
  { getCatAlgPairs, deleteCatAlgPair }
)(CatAlgPairs);
