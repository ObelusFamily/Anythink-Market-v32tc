import React from "react";
import logo from "../../imgs/logo.png";
import SearchBar from "./SearchBar"

const Banner = () => {
  return (
    <div className="banner text-white">
      <div className="container p-4 text-center">
        <img src={logo} alt="banner" />
        <div style={{fontSize: "20px"}}>
          <span id="get-part">A place to get</span> &nbsp;
          <SearchBar/>
          <span> the cool stuff.</span>
        </div>
      </div>
    </div>
  );
};

export default Banner;
