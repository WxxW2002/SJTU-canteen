import createElement from "./../assets/lib/create-element.js";

export default class StepSlider {
  constructor({ steps, value = 0 }) {
    this.steps = steps;
    this.segments = steps - 1;
    this.render();
    this.thumb = this.elem.querySelector(".slider__thumb");
    this.progress = this.elem.querySelector(".slider__progress");
    this.addEventListeners();
    this.setValue(value);
  }
  render() {
    this.elem = createElement(`
    <div class="slider">
      <div class="slider__thumb" style="left: 50%">
        <span class="slider__value"></span>
      </div>
      <div class="slider__progress" style="width: 50%"></div>
      <div class="slider__steps">
      ${"<span></span>".repeat(this.steps)}
      </div>
  </div>
    `);
  }

  setValue = (value) => {
    this.value = value;

    this.elem.querySelector(".slider__value").innerHTML = this.value;

    let childrens = this.elem.querySelector(".slider__steps").children;

    for (let children of childrens) {
      children.classList.remove("slider__step-active");
    }

    let procentValue = (value / this.segments) * 100;

    this.thumb.style.left = `${procentValue}%`;
    this.progress.style.width = `${procentValue}%`;

    childrens[this.value].classList.add("slider__step-active");
  };

  addEventListeners = () => {
    this.thumb.ondragstart = () => false;
    this.thumb.addEventListener("pointerdown", this.onPointerDown);
    this.elem.addEventListener("click", this.onClick);
  };

  onClick = (event) => {
    let newLeft =
      (event.clientX - this.elem.getBoundingClientRect().left) /
      this.elem.offsetWidth;
    this.setValue(Math.round(this.segments * newLeft));

    this.elem.dispatchEvent(
      new CustomEvent("slider-change", {
        detail: this.value,
        bubbles: true,
      })
    );
  };

  onPointerDown = (event) => {
    event.preventDefault();

    this.elem.classList.add("slider_dragging");

    document.addEventListener("pointermove", this.onPointerMove);
    document.addEventListener("pointerup", this.onPointerUp);
  };

  onPointerMove = (event) => {
    event.preventDefault();
    let newLeft = this.calcLeftByEvent(event);

    this.thumb.style.left = `${newLeft * 100}%`;
    this.progress.style.width = `${newLeft * 100}%`;

    this.value = Math.round(this.segments * newLeft);
    this.elem.querySelector(".slider__value").innerHTML = this.value;

    let childrens = this.elem.querySelector(".slider__steps").children;

    for (let children of childrens) {
      children.classList.remove("slider__step-active");
    }

    childrens[this.value].classList.add("slider__step-active");
  };

  onPointerUp = () => {
    document.removeEventListener("pointermove", this.onPointerMove);
    document.removeEventListener("pointerup", this.onPointerUp);

    this.elem.classList.remove("slider_dragging");

    this.thumb.style.left = `${(this.value / this.segments) * 100}%`;
    this.progress.style.width = `${(this.value / this.segments) * 100}%`;

    this.elem.dispatchEvent(
      new CustomEvent("slider-change", {
        detail: this.value,
        bubbles: true,
      })
    );
  };

  calcLeftByEvent(event) {
    let newLeft =
      (event.clientX - this.elem.getBoundingClientRect().left) /
      this.elem.offsetWidth;

    if (newLeft < 0) {
      newLeft = 0;
    }
    if (newLeft > 1) {
      newLeft = 1;
    }

    return newLeft;
  }
}
