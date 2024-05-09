function myFunction() {
  let input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1]; // Choose the column you want to filter
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

function collapse() {
  const sidebar = document.querySelector(".sidebar");
  const sidebarListItem = document.querySelectorAll(".sidebar-list-item");
  const leftArrow = document.querySelector(".collapse-button-left");
  const rightArrow = document.querySelector(".collapse-button-right");
  const main = document.querySelector(".content");

    sidebar.classList.toggle("collapse-sidebar");
    main.classList.toggle("expand-content");
    leftArrow.classList.toggle("d-none");
    rightArrow.classList.toggle("d-none");
    sidebarListItem.forEach((item) => {
      item.classList.toggle("d-none");
    });
}


function deleteStaff() {
  const deleteButton = document.getElementsByClassName("deleteStaffCheck");
  
  for (let i = 0; i < deleteButton.length; i++) {
    deleteButton[i].classList.toggle("deleteStaffCheckNone");
  }
}