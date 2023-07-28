const qrForm = document.querySelector("#qr-form")
const qrUrl = document.querySelector("#qr-url")
const formCSRF = document.getElementsByName("csrfmiddlewaretoken")
const qrImage = document.getElementById("qr-image")
const qrDownload = document.getElementById("qr-download")


console.log(qrDownload.href)
qrForm.addEventListener("submit", (e)=>{
    e.preventDefault();
    const form = new FormData();
    form.append('csrfmiddlewaretoken', formCSRF[0].value);
    form.append('url', qrUrl.value)
    
    $.ajax({
        type:'POST',
        url:'/create_request',
        data:form,
        success:function(response){
            qrImage.classList.remove('display')
            qrDownload.classList.remove('display')
            qrImage.src = response.qr
            qrDownload.href = response.qr
        },
        error:function(error){
            console.log(error)
        },
        cache:false,
        contentType:false,
        processData:false,
    })
})