const us = document.getElementById("username");
const pas = document.getElementById("password");
const error = document.getElementById("error");

us.addEventListener("input", () => {
  error.innerHTML = "";
});

pas.addEventListener("input", () => {
  error.innerHTML = "";
});
async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  await fetch("http://localhost:3000/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      if (data.success) {
        if (data.userType === "admin") {
          window.location.href = "/dashboard/admin/admin_dashboard.html";
        } else {
          window.location.href = "/dashboard/user/user.html";
        }
      } else {
        error.innerHTML = "Wrong password !!";
      }
    })
    .catch((error) => {
      alert("Error: " + error);
    });
}
