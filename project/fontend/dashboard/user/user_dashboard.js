// const div = document.querySelector(".result");
// // Function to handle form submission
// function submitHelpdeskRequest() {
//   const form = document.getElementById("helpdeskForm");

//   // Get form data as an object
//   const formData = {
//     name: form.elements["name"].value,
//     email: form.elements["email"].value,
//     subject: form.elements["subject"].value,
//     message: form.elements["message"].value,
//   };

//   // Send form data to the server using Fetch API
//   fetch("http://localhost:3000/submitHelpdeskRequest", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(formData),
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       if (data.success) {
//         // Form submission successful
//         alert("Helpdesk request submitted successfully.");
//         form.reset(); // Reset the form after successful submission
//       } else {
//         alert("Failed to submit helpdesk request.");
//       }
//     })
//     .catch((error) => {
//       alert("Error: " + error);
//     });
// }

// // Function to fetch helpdesk requests from the backend and display them on the page
// async function fetchAndDisplayHelpdeskRequests() {
//   await fetch("http://localhost:3000/getHelpdeskRequests") // Replace with your backend API endpoint for fetching helpdesk requests
//     .then((response) => response.json())
//     .then((data) => {
//       div.innerHTML = "";
//       let arry = data.helpdeskRequests;
//       for (let i = 0; i < arry.length; i++) {
//         const card = document.createElement("div");
//         card.classList.add("card");
//         const name = document.createElement("p");
//         name.textContent = `Name: ${arry[i].name}`;
//         const email = document.createElement("p");
//         email.textContent = `Email: ${arry[i].email}`;
//         const subject = document.createElement("p");
//         subject.textContent = `Subject: ${arry[i].subject}`;
//         const message = document.createElement("p");
//         message.textContent = `Message: ${arry[i].message}`;

//         card.appendChild(name);
//         card.appendChild(email);
//         card.appendChild(subject);
//         card.appendChild(message);
//         div.appendChild(card);
//       }
//     });
// }

// // Add event listener to submit button of the form
// const submitButton = document.getElementById("submitBtn"); // Replace 'submitBtn' with the ID of your submit button
// submitButton.addEventListener("click", (event) => {
//   event.preventDefault(); // Prevent form submission via traditional form submission
//   submitHelpdeskRequest();
// });

// const btn = document.getElementById("btn");
// btn.addEventListener("click", (e) => {
//   e.preventDefault();
//   fetchAndDisplayHelpdeskRequests();
// });

const form = document.querySelector("#form");
function openForm() {
  form.style.display = "block";
}

function closeForm() {
  form.style.display = "none";
}
