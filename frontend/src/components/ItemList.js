import ItemPreview from "./ItemPreview";
import ListPagination from "./ListPagination";
import React from "react";

const ItemList = (props) => {
  if (!props.items) {
    return <div className="py-4">Loading...</div>;
  }

  if (props.items.length === 0) {
    if (props.title == "") {
      return <div className="py-4 no-items">No items are here... yet.</div>;
    }
    return (
      <div
        className="py-4 no-items text-center"
        style={{ backgroundColor: "rgba(255,255,255,0.1)" }}
      >
        <i
          className="bi bi-emoji-frown-fill text-white"
          style={{ fontSize: "36px" }}
        ></i>
        <div id="empty">No items found for "{props.title}"</div>
      </div>
    );
  }

  return (
    <div className="container py-2">
      <div className="row">
        {props.items.map((item) => {
          return (
            <div className="col-sm-4 pb-2" key={item.slug}>
              <ItemPreview item={item} />
            </div>
          );
        })}
      </div>

      <ListPagination
        pager={props.pager}
        itemsCount={props.itemsCount}
        currentPage={props.currentPage}
      />
    </div>
  );
};

export default ItemList;
