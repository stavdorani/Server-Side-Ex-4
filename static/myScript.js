try {
    const contant_header_con = document.getElementById("contant_header_con");
    contant_header_con.addEventListener("mouseover", changeBorderStyle2);
    contant_header_con.addEventListener("mouseleave", changeBorderColor);
  } catch (error) {
    console.error(error);
    // expected output: ReferenceError: nonExistentFunction is not defined
    // Note - error messages will vary depending on browser
  }

try {
    const contant_header_hom = document.getElementById("contant_header");
    const borderColor = contant_header_hom.style.borderColor;
    contant_header_hom.addEventListener("mouseover", changeBorderStyle);
    contant_header_hom.addEventListener("mouseleave", changeBorderColor);
} catch (error) {
console.error(error);
// expected output: ReferenceError: nonExistentFunction is not defined
// Note - error messages will vary depending on browser
}

function changeBorderStyle2(){
    this.style.borderRadius = "15px" ;
    this.style.borderStyle = "dotted";
    this.style.color = "rgb(80, 86, 87)";
}
function changeBorderColor(){
    this.style.color = "rgb(31, 195, 222)";
}


function changeBorderStyle(){
    this.style.borderRadius = "15px" ;
    this.style.borderStyle = "dashed";
    this.style.color = "rgb(0, 78, 100)";
}

const navHom = document.getElementById("hom");
const navCon = document.getElementById("con");
const navAss1 = document.getElementById("ass31");
const navAss2 = document.getElementById("ass32");
const navAss4 = document.getElementById("ass4");

function markThis(eleme){
    eleme.style.color = "green";
    eleme.style.fontSize = "25px";
}

if ( document.URL.includes("home") ) {
    markThis(navHom);
} else if (document.URL.includes("contact")) {
    markThis(navCon);
} else if (document.URL.includes("3_1")) {
    markThis(navAss1);
} else if (document.URL.includes("3_2")) {
    markThis(navAss2);
} else  {
    markThis(navAss4);
}


document.querySelector('#front_form')?.addEventListener('submit',(e)=> {
    e.preventDefault()
    const id = e.target.id.value
    fetch('https://reqres.in/api/users/' + id)
        .then(results => results.json())
        .then(json => {
            const name = document.querySelector('#front_form_name')
            const email = document.querySelector('#front_form_email')
            name.innerHTML = json.data.first_name + " " + json.data.last_name
            email.innerHTML = json.data.email
            name.removeAttribute("hidden")
            email.removeAttribute("hidden")
        })
        .catch((e) => {
        console.log(e)
        })
})