const emailField = document.getElementById("EmailField");
const passwordField = document.getElementById("PasswordField");
const keepLoggedIn = document.getElementById("KeepLoggedIn");
const loginBtn = document.getElementById("loginBtn");
const errorMsg = document.getElementById("errorMsg");
function loginUser() {
  console.log("loginUser");
  const email = emailField.value;
  const password = passwordField.value;
  console.log(keepLoggedIn);
  // check if input is checked
  const loginData = {
    email: email,
    password: password,
    keepLoggedIn: keepLoggedIn,
  };
  const loginUrl = "http://localhost:8000/auth/login";
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("POST", loginUrl, true);
  xmlhttp.setRequestHeader("Content-type", "application/json");
  xmlhttp.send(JSON.stringify(loginData));
  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        //window.location.href = "/profile/" + username.value;
        console.log("login success");
      } else {
        //errorMsg.innerHTML = "Invalid username or password";
        console.log("error");
      }
    }
  };
}
loginBtn.addEventListener("click", loginUser);
//# sourceMappingURL=auth-login.js.map

password.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    loginBtn.click();
  }
});
