document.getElementById("contactForm").addEventListener("submit", function(e){
    e.preventDefault();

    fetch("/api/contact/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: document.getElementById("name").value,
            email: document.getElementById("email").value,
            phone: document.getElementById("phone").value,
            message: document.getElementById("message").value
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        document.getElementById("contactForm").reset();
    });
});
