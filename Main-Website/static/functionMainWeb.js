the_heading = document.getElementById("Title");
//function that redirects user to Rickroll video
function rickRoll() {
    window.location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley";
}
//Retrieves input from search bar, and compiles it into a link, to redirect user to output page
function search() {
    var searchedWord = document.getElementById("user-search").value;
    var compiledSearchLink = "/display/" + searchedWord;
    window.location.href = compiledSearchLink;
}
//Retrieves input dropdwon menus, and compiles it into a link, to redirect user to output page
function submitCompiledLink() {
    // Get selected values from dropdowns
    var brand = document.getElementById("brand").value;
    var ram = document.getElementById("ram").value;
    var storage = document.getElementById("storage").value;
    //var price = document.getElementById("price").value;
    var screenSize = document.getElementById("screenSize").value;
    var touchScreen = document.getElementById("touchScreen").value;
    // Construct the URL based on selected values
    var compiledLink = "/display/" 
    + brand 
    + "/" + ram 
    + "/" + storage 
    //+ "/" + price 
    + "/" + screenSize 
    + "/" + touchScreen;

console.log(brand)

    // Redirect to the compiled link
    //window.location.href = compiledLink;
}

