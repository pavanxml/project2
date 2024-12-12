
const inpTags = document.getElementsByTagName("input")

for (let tag = 0; tag < inpTags.length; tag++) {
    const element = inpTags[tag];
    element.addEventListener("mouseover", function(){
        element.style.boxShadow = "4px 4px 10px aliceblue";
        element.style.backgroundColor = "rgba(70, 67, 67, 0.248)";
    })

    element.addEventListener("mouseleave", function(){
        element.style.boxShadow = "";
        element.style.backgroundColor = "";

    })
    
}
