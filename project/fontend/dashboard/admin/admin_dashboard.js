const output = document.querySelector(".addData");
const progress = document.querySelector(".progress");
document.addEventListener("DOMContentLoaded", function () {
  fetchAndDisplayHelpdeskRequests();
});

async function fetchAndDisplayHelpdeskRequests() {
  await fetch("http://localhost:3000/getHelpdeskRequests") // Replace with your backend API endpoint for fetching helpdesk requests
    .then((response) => response.json())
    .then((data) => {
      const arry = data.helpdeskRequests;
      for (let i = 0; i < arry.length; i++) {
        let tr = document.createElement("tr");
        tr.innerHTML = `
<td>${arry[i].id}</td>
<td>${arry[i].name}</td>
<td>${arry[i].email}</td>
<td>${arry[i].operating}</td>
<td>${arry[i].subject}</td>
<td>${arry[i].status}</td>
<td>${arry[i].created_at}</td>
<td>

  <button
    class="view-button"
    onclick="showPopup('Subject: ${escapeHtml(arry[i].subject)}', '${escapeHtml(
          arry[i].message
        )}', ${arry[i].id})"
  >
    View
  </button>
</td>`;
        output.appendChild(tr);
      }
    });
}

function escapeHtml(unsafe) {
  return unsafe.replace(/[&<"'>]/g, function (match) {
    switch (match) {
      case "&":
        return "&amp;";
      case "<":
        return "&lt;";
      case ">":
        return "&gt;";
      case '"':
        return "&quot;";
      case "'":
        return "&#039;";
    }
  });
}

let ids;

function showPopup(title, description, id) {
  document.getElementById("popup-title").innerText = title;
  document.getElementById("popup-description").innerText = description;
  document.getElementById("popup").style.display = "flex";
  ids = id;
}

function closePopup() {
  document.getElementById("popup").style.display = "none";
}

function updateStatus(status) {
  const requestId = ids; // The ID of the helpdesk request you want to update

  fetch("http://localhost:3000/updateHelpdeskRequest", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ requestId, status }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data.message);
      // You can perform additional actions here based on the response
    })
    .catch((error) => {
      console.error("Error updating the request:", error);
      // Handle the error, if any
    });
  closePopup();
}
