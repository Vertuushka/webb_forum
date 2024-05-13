$(document).ready(function() {
    function onWindowResize() {
        $('body').css('height', `${window.innerHeight}px`)
    }

    onWindowResize();
    window.addEventListener('resize', onWindowResize);
    var warnBtn = document.querySelectorAll(".warnBtn");
    warnBtn.forEach(function(button){
        button.onclick = function()
        {
            var id = this.parentElement.parentElement.parentElement.parentElement.getAttribute("id")
            document.querySelector(".content").appendChild(CreateWarningForm(id, 0, GetCsrfToken()))
        }
    });
});

function GetCsrfToken()
{
    var token = document.querySelector("#token");
    csrf = token.getAttribute("value");
    return csrf
}

function CreateWarningForm(message_id, is_first_message, csrf_token)
{
    var form = document.createElement("form");
    form.setAttribute("action", "");
    form.setAttribute("method", "post")
  
    var csrfToken = document.createElement("input");
    csrfToken.setAttribute("type", "hidden");
    csrfToken.setAttribute("name", "csrfmiddlewaretoken");
    csrfToken.setAttribute("value", csrf_token);
    form.appendChild(csrfToken);
  
    var reasonLabel = document.createElement("label");
    reasonLabel.innerText = "Reason:";
    form.appendChild(reasonLabel);
  
    var reasonInput = document.createElement("input");
    reasonInput.setAttribute("type", "text");
    reasonInput.setAttribute("name", "warning_reason");
    form.appendChild(reasonInput);
  
    var deleteCheckbox = document.createElement("input");
    deleteCheckbox.setAttribute("type", "checkbox");
    deleteCheckbox.setAttribute("id", "deleteMessage");
    deleteCheckbox.setAttribute("name", "is_deleted");
    form.appendChild(deleteCheckbox);
  
    var deleteLabel = document.createElement("label");
    deleteLabel.setAttribute("for", "deleteMessage");
    deleteLabel.innerText = "Delete this message as well";
    form.appendChild(deleteLabel);
  
    var deleteReasonInput = document.createElement("input");
    deleteReasonInput.setAttribute("type", "text");
    deleteReasonInput.setAttribute("name", "deleting_reason");
    deleteReasonInput.setAttribute("placeholder", "Reason:");
    form.appendChild(deleteReasonInput);

    var notificationLabel = document.createElement("label");
    notificationLabel.setAttribute("for", "is_notified");
    notificationLabel.innerText = "Send notification";
    form.appendChild(notificationLabel);

    var notificationInput = document.createElement("input");
    notificationInput.setAttribute("type", "text");
    notificationInput.setAttribute("name", "notification");
    form.appendChild(notificationInput)

    var submitButton = document.createElement("input");
    submitButton.setAttribute("type", "submit");
    submitButton.setAttribute("value", "Warn");
    form.appendChild(submitButton);
    
  
    return form; 
}

