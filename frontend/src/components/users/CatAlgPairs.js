import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getCatAlgPairs } from "../../actions/catAlgPairs";

export class CatAlgPairs extends Component {
  static propTypes = {
    catAlgPairs: PropTypes.array.isRequired
  };

  componentDidMount() {
    this.props.getCatAlgPairs();
  }

  render() {
    return (
      <Fragment>
        <div>
          <h2>Categories and Algorithms</h2>
          <table className="table table-striped">
            <thead>
              <tr>
                <th>Category</th>
                <th>Algorithm</th>
                {/* for deletion: */}
                <th />
              </tr>
            </thead>
            <tbody>
              {this.props.catAlgPairs.map(catAlgPair => (
                <tr key={catAlgPair.id}>
                  <td>{catAlgPair.category}</td>
                  <td>{catAlgPair.algorithm}</td>
                  <td>
                    <button className="btn btn-danger btn-sm">Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  catAlgPairs: state.catAlgPairs.catAlgPairs // get reducer, then get its actual catAlgPairs
});

export default connect(
  mapStateToProps,
  { getCatAlgPairs }
)(CatAlgPairs);
