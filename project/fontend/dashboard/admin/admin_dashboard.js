const div = document.getElementById("result");
async function fetchAndDisplayHelpdeskRequests() {
  await fetch("http://localhost:3000/getHelpdeskRequests") // Replace with your backend API endpoint for fetching helpdesk requests
    .then((response) => response.json())
    .then((data) => {
      div.innerHTML = "";
      let arry = data.helpdeskRequests;
      for (let i = 0; i < arry.length; i++) {
        const card = document.createElement("div");
        card.classList.add("card");
        const name = document.createElement("p");
        name.textContent = `Name: ${arry[i].name}`;
        const email = document.createElement("p");
        email.textContent = `Email: ${arry[i].email}`;
        const subject = document.createElement("p");
        subject.textContent = `Subject: ${arry[i].subject}`;
        const message = document.createElement("p");
        message.textContent = `Message: ${arry[i].message}`;

        card.appendChild(name);
        card.appendChild(email);
        card.appendChild(subject);
        card.appendChild(message);
        div.appendChild(card);
      }
    });
}

const button = document.getElementById("adbtn");
button.addEventListener("click", (e) => {
  e.preventDefault();
  fetchAndDisplayHelpdeskRequests();
});
