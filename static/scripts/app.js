document.getElementById("tryonForm").addEventListener("submit", function (event) {
    event.preventDefault();

    let formData = new FormData();
    formData.append("person_image", document.getElementById("person_image").files[0]);
    formData.append("dress_image", document.getElementById("dress_image").files[0]);

    fetch("/upload", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.result) {
            const resultImage = document.getElementById("result-image");
            resultImage.src = data.result;
            resultImage.style.display = "block";
        } else {
            alert("Error: " + data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
