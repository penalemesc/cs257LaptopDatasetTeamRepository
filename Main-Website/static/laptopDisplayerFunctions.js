
function onLoadFunct() {
    // Grab the brand, ram, storage from the URL
    // GET THE JSON from the Flask server
    // Call Generate Display
    const pathstring = location.pathname;
    const pathlist = pathstring.split('/');
    const brand = pathlist[2];
    const ram = pathlist[3];
    const storage = pathlist[4];

    console.log("onLoad: " + brand + " " + ram + " " + storage);

    const queryURL = `/json/${brand}/${ram}/${storage}`;
    fetch(queryURL)
        .then(response => response.json())
        .then(data => generateDisplay(data))
        .catch(error => console.error('Error fetching data:', error));
}
function onloadSearchFunct() {
    // Grab the searched word from the URL
    // GET THE JSON from the Flask server
    // Call Generate Display
    const searchPathstring = location.pathname;
    const searchPathlist = searchPathstring.split('/');
    const searchedWord = searchPathlist[2];

    const queryURL = `/search/${searchedWord}`;
    fetch(queryURL)
        .then(response => response.json())
        .then(data => generateDisplay(data))
        .catch(error => console.error('Error fetching data:', error));

}

//Locates the html location, and creates html from JSON data
//Also appends the newly created html into the output html files to display
//This file needs to be worked on to properly display the correct image for 
//each laptop
function generateDisplay(data) {
    if (!data.nameForLaptop || !data.priceForLaptop) {
        // Display an error message if the expected data is not found
        const container = document.getElementById("myDIV");
        const errorMsg = document.createElement("p");
        errorMsg.innerText = "No laptops found or an error occurred.";
        container.appendChild(errorMsg);
        return;
    }

    const laptopNames = data.nameForLaptop;
    const laptopPrices = data.priceForLaptop;
    const laptop_CPU = data.CpuForLaptop
    const laptop_RAM = data.RamForLaptop
    const laptop_screensize = data.screensizeLaptop
    const laptop_touchscreen = data.touchscreenLaptop

    console.log(laptopNames);
    console.log(laptopPrices);
    console.log(laptop_CPU);
    console.log(laptop_RAM);
    console.log(laptop_screensize);
    console.log(laptop_touchscreen);

    const container = document.getElementById("myDIV");
    container.innerHTML = ''; // Clear previous contents

    for (let i = 0; i < laptopNames.length; i++) {

        const div = document.createElement("div");
        div.className = 'profile-card';
        
        let pic = document.createElement('img');
        pic.src = "/static/LaptopImages/laptop_3.png";
        pic.className = 'profile-pic';

        const profileDetails = document.createElement('div');
        profileDetails.className = 'profile-details';

        const title = document.createElement('h2');
        title.textContent = laptopNames[i];

        const info = document.createElement('p');
        info.className = 'laptopText-class';
        info.id = 'laptopInfo';
        info.innerHTML =  `
                    <strong>Name of Laptop:</strong>  <br>
                    <strong>Price of Laptop:</strong> ${laptopPrices[i]} <br>
                    <strong>Ram:</strong> ${laptop_RAM[i]} <br>
                    <strong>Screen Size:</strong> ${laptop_screensize}
                `;

        profileDetails.appendChild(title);
        profileDetails.appendChild(info);
        div.appendChild(pic);
        div.appendChild(profileDetails);
        
        // Append to myDIV:
        container.appendChild(div);
    }
}