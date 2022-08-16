import React from "react";
import { useState } from "react";
import { connect } from "react-redux";
import agent from "../../agent";
import { NEW_TITLE_FILTER } from "../../constants/actionTypes";

const mapDispatchToProps = (dispatch) => ({
  onSearchTitle: (title, pager, payload) => {
    return dispatch({ type: NEW_TITLE_FILTER, title, pager, payload });
  },
});

const SearchBar = (props) => {
  let [title, setTitle] = useState("");

  const onTitleChange = (event) => {
    let newTitle = event.target.value;
    event.preventDefault();
    setTitle(newTitle);
    props.onSearchTitle(
      event.target.value,
      agent.Items.byTitle,
      agent.Items.byTitle(newTitle)
    );
  };
  if (!props.show){
    return ''
  }

  return (
    <span>
        &nbsp;
      <input
        id="search-box"
        className="search-by-title form-control-lg"
        type="text"
        placeholder="What is it that you truly desire?"
        value={title}
        onChange={onTitleChange}
      />
      <i className="bi bi-search search-icon"></i>
    </span>
  );
};

export default connect(null, mapDispatchToProps)(SearchBar);
