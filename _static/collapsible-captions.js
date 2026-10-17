document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("p.caption").forEach(function (caption) {
    const list = caption.nextElementSibling;
    if (!list || list.tagName !== "UL") return;

    caption.classList.add("collapsible-caption");

    const hasCurrentPage = list.querySelector(".current, .active");
    if (!hasCurrentPage) {
      list.style.display = "none";
      caption.classList.add("collapsed");
    }

    caption.addEventListener("click", function () {
      const isHidden = list.style.display === "none";
      list.style.display = isHidden ? "" : "none";
      caption.classList.toggle("collapsed", !isHidden);
    });
  });
});
