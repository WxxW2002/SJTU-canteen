import createElement from "./../assets/lib/create-element.js";

export default class Carousel {
  constructor(slides) {
    this.slides = slides;

    this.render();
    this.addEventListeners();
    this.counter = 0;
    this.position = 0;
    this.movePosition = 988;
    this.slideLine = this.elem.querySelector(".carousel__inner");
    this.btnPrev = this.elem.querySelector(".carousel__arrow_left");
    this.btnNext = this.elem.querySelector(".carousel__arrow_right");
    this.watchCounter();
  }

  render() {
    this.elem = createElement(`
        <div class="carousel">
          <div class="carousel__arrow carousel__arrow_right">
            <img src="/ranking/assets/images/icons/angle-icon.svg" alt="icon" />
          </div>
          <div class="carousel__arrow carousel__arrow_left">
            <img src="/ranking/assets/images/icons/angle-left-icon.svg" alt="icon" />
          </div>
          <div class="carousel__inner"></div>
        </div>
        `);

    let slides = this.slides.map((item) =>
      createElement(`
      <div class="carousel__slide" data-id="${item.id}">
        <img
          src="/ranking/assets/images/carousel/${item.image}"
          class="carousel__img"
          alt="slide"
        />
        <div class="carousel__caption">
          <span class="carousel__price">¥${item.price.toFixed(2)}</span>
          <div class="carousel__title">${item.name}</div>
        <!-- <button type="button" class="carousel__button">
        ¥${item.price.toFixed(2)}
        </button> -->
        </div>
      </div>`)
    );
    this.sub("inner").append(...slides);
  }

  sub(ref) {
    return this.elem.querySelector(`.carousel__${ref}`);
  }

  setPosition() {
    this.slideLine.style.transform = `translateX(${this.position}px)`;
  }

  addEventListeners() {
    const BtnPrev = this.elem.querySelector(".carousel__arrow_left");
    BtnPrev.addEventListener("click", () => {
      this.counter--;
      this.position += this.movePosition;
      this.setPosition();
      this.watchCounter();
    });

    const BtnNext = this.elem.querySelector(".carousel__arrow_right");
    BtnNext.addEventListener("click", () => {
      this.counter++;
      this.position -= this.movePosition;
      this.setPosition();
      this.watchCounter();
    });

    this.elem.onclick = ({ target }) => {
      let button = target.closest(".carousel__button");
      
      if (button) {
        let id = target.closest("[data-id]").dataset.id;

        this.elem.dispatchEvent(
          new CustomEvent("product-add", {
            detail: id,
            bubbles: true,
          })
        );
      }
    };
  }

  watchCounter() {
    if (this.counter == 0) {
      this.btnPrev.style.display = "none";
    } else {
      this.btnPrev.style.display = "";
    }

    if (this.counter == this.slides.length - 1) {
      this.btnNext.style.display = "none";
    } else {
      this.btnNext.style.display = "";
    }
  }
}
