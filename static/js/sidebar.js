document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const openBtn = document.getElementById("openSidebar");
  const closeBtn = document.getElementById("closeSidebar");

  openBtn.addEventListener("click", function () {
    sidebar.classList.add("open");
  });

  closeBtn.addEventListener("click", function () {
    sidebar.classList.remove("open");
  });
});
