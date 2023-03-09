import createElement from "./../assets/lib/create-element.js";

export default class Modal {
  constructor() {
    this.render();
    this.modalBody = this.elem.querySelector(".modal__body");
    this.btnClose = this.elem.querySelector(".modal__close");
    this.addEventListeners();
  }

  render() {
    this.elem = createElement(`
      <div class="modal">
        <div class="modal__overlay"></div>
        <div class="modal__inner">
          <div class="modal__header">
            <button type="button" class="modal__close">
              <img src="/ranking/assets/images/icons/cross-icon.svg" alt="close-icon" />
            </button>
            <h3 class="modal__title"></h3>
          </div>
          <div class="modal__body"></div>
        </div>
      </div>
    `);
  }

  addEventListeners() {
    this.btnClose.addEventListener("click", this.onClick);
    document.addEventListener("keydown", this.onDocumentKeyDown);
  }

  open() {
    document.body.append(this.elem);
    document.body.classList.add("is-modal-open");
  }

  onClick = (event) => {
    event.preventDefault();
    this.close();
  };

  onDocumentKeyDown = (event) => {
    if (event.code === "Escape") {
      event.preventDefault();
      this.close();
    }
  };

  setTitle(title) {
    this.elem.querySelector(".modal__title").textContent = title;
  }

  setBody = (node) => {
    this.modalBody.innerHTML = "";
    this.modalBody.append(node);
  };

  close = () => {
    document.body.classList.remove("is-modal-open");
    this.elem.remove();
  };
}
