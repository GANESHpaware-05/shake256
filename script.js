 function myFunction1() {
            // Get the text field
            var copyText = document.getElementById("shake256_output");

            // Select the text field
            copyText.select();
            copyText.setSelectionRange(0, 99999); // For mobile devices

            // Copy the text inside the text field
            navigator.clipboard.writeText(copyText.value);

            document.getElementById("copy").innerText="Value Copied !!"; 
 }
    