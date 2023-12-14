//Variable declaration

let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);

let email = id("email"),
    phone = id("phoneNumber"),
    username = id("username"),
    password = id("password"),
    comfirm = id("comfirmPassword"),
    form = id("form"),
    errorMsg = classes("error"),
    successIcon = classes("success-icon"),
    failureIcon = classes("failure-icon");

    

//   form.addEventListener("submit", (e) => {
//     e.preventDefault();

form.addEventListener('input', (e) => {
        // e.preventDefault();
    
    emailValidator(email,0,"Please enter a valid email");
    phoneNumberValidator(phoneNumber,1,"Please type a phone number");
    validator(username,2,"Please enter a username");
    validator(password,3,"Password cannot be blank");
    passwordValidator(comfirmPassword,4,"Please comfirm password again");
    
    });

let emailValidator = (id,serial,message) => {
    if(id.value.trim() === ''){
        errorMsg[serial].innerHTML = message;
        failureIcon[serial].style.opacity = "1";
        successIcon[serial].style.opacity = "0";
      }else if (id.value.length < 3){
        errorMsg[serial].innerHTML = message;
        successIcon[serial].style.opacity = "0";
        failureIcon[serial].style.opacity = "1";
      }else if(id.value.includes("@")){
        errorMsg[serial].innerHTML = "";
        failureIcon[serial].style.opacity = "0";
        successIcon[serial].style.opacity = "1";
      }else{
        errorMsg[serial].innerHTML = "Pleaseinclude the @ sign";
        successIcon[serial].style.opacity = "0";
        failureIcon[serial].style.opacity = "1";
      }
}

let phoneNumberValidator = (id,serial,message) => {

    if(id.value.trim() === '' 
    || id.value.length < 11){
      errorMsg[serial].innerHTML = message;
      failureIcon[serial].style.opacity = "1";
      successIcon[serial].style.opacity = "0";
    }else{
      errorMsg[serial].innerHTML = "";
      successIcon[serial].style.opacity = "1";
      failureIcon[serial].style.opacity = "0";
    }
  }

let validator = (id,serial,message) => {

  if(id.value.trim() === ''){
    errorMsg[serial].innerHTML = message;
    failureIcon[serial].style.opacity = "1";
    successIcon[serial].style.opacity = "0";
  }else{
    errorMsg[serial].innerHTML = "";
    successIcon[serial].style.opacity = "1";
    failureIcon[serial].style.opacity = "0";
  }
}





let passwordValidator = (id,serial,message) => {

    if ((password.value.trim() === '' 
    && comfirmPassword.value.trim() === '')
    || comfirmPassword.value != password.value){
        errorMsg[serial].innerHTML = "It does not correspond with your password above";
        successIcon[serial].style.opacity = "0";
        failureIcon[serial].style.opacity = "1";
    }
    else{
        errorMsg[serial].innerHTML = '';
        successIcon[serial].style.opacity = "1";
        failureIcon[serial].style.opacity = "0";
    }
}