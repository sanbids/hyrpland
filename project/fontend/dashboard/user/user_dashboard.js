const output = document.querySelector(".added");
const form = document.querySelector("#form");

document.addEventListener("DOMContentLoaded", function () {
  getData();
});

function submitHelpdeskRequest() {
  // Get form data as an object
  const formData = {
    name: form.elements["name"].value,
    email: form.elements["email"].value,
    operating: form.elements["operating"].value,
    subject: form.elements["subject"].value,
    message: form.elements["message"].value,
  };

  // Send form data to the server using Fetch API
  fetch("http://localhost:3000/submitHelpdeskRequest", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(formData),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        // Form submission successful
        alert("Helpdesk request submitted successfully.");
        form.reset(); // Reset the form after successful submission
      } else {
        alert("Failed to submit helpdesk request.");
      }
    })
    .catch((error) => {
      alert("Error: " + error);
    });
}

// // Function to fetch helpdesk requests from the backend and display them on the page
async function getData() {
  console.log("fetching");
  await fetch("http://localhost:3000/getHelpdeskRequests")
    .then((response) => response.json())
    .then((data) => {
      const arry = data.helpdeskRequests;
      for (let i = 0; i < arry.length; i++) {
        let tr = document.createElement("tr");
        tr.innerHTML = `
          <td><input type="checkbox" /></td>
          <td>${arry[i].name}</td>
          <td>${arry[i].email}</td>
          <td>${arry[i].operating}</td>
          <td>${arry[i].subject}</td>
          <td>${arry[i].status}</td>
          <td>
            <button
              class="view-button"
              onclick="showPopup('${escapeHtml(
                arry[i].subject
              )}', '${escapeHtml(arry[i].message)}')"
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

// Add event listener to submit button of the form
const submitButton = document.getElementById("form_button"); // Replace 'submitBtn' with the ID of your submit button
submitButton.addEventListener("click", (event) => {
  event.preventDefault(); // Prevent form submission via traditional form submission
  submitHelpdeskRequest();
});

const mainForm = document.querySelector(".mainForm");

function openForm() {
  mainForm.style.display = "block";
}

function closeForm() {
  mainForm.style.display = "none";
}

function showPopup(title, description) {
  document.getElementById("popup-title").innerText = title;
  document.getElementById("popup-description").innerText = description;
  document.getElementById("popup").style.display = "flex";
}

function closePopup() {
  document.getElementById("popup").style.display = "none";
}
