 import createElement from "./../assets/lib/create-element.js";
import escapeHtml from "./../assets/lib/escape-html.js";

export default class ProductCard {
  constructor(product) {
    this.product = product;
    this.render();
    this.addEventListeners();
  }

  addEventListeners = () => {
    let button = this.elem.querySelector(".card__button");
    button.addEventListener("click", this.onClick);
  };

  onClick = () => {
    let customEvent = new CustomEvent("product-add", {
      bubbles: true,
      detail: this.product.id,
    });
    this.elem.dispatchEvent(customEvent);
  };

  render() {
    this.elem = createElement(`<div class="card">
      <div class="card__top">
        <img
          src="/ranking/assets/images/products/${this.product.image}"
          class="card__image"
          alt="product"
        />
       <span class="card__stars">${this.product.spiciness.toFixed(2)}</span>
      </div>
      <div class="card__body">
        <div class="card__title">${escapeHtml(this.product.name)}</div>
        <button type="button" class="card__button">
        <span class="card__price">¥${this.product.price.toFixed(2)}</span>
        </button>
      </div>
    </div>`);
  }
}
