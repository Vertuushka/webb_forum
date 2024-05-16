$(document).ready(function() {
    console.log("123")
    function onWindowResize() {
        $('body').css('height', `${window.innerHeight}px`)
    }

    onWindowResize();
    window.addEventListener('resize', onWindowResize);

    // warning btn
    $(".warnBtn").each(function(index, button){
        let msg = this.parentElement.parentElement.parentElement.lastElementChild.innerHTML;
        let id = this.parentElement.parentElement.parentElement.parentElement.getAttribute("id");
        this.addEventListener('click', function(){
            $("body").append(`
            <form action="/forum/message/${id}/warn/" method="post" id="warnForm">
                <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                <label for="warn_reason">Warning reason:</label>
                <input type="text" name="warn_reason" id="">
                <label for=""><input type="checkbox" name="is_deleted" id="">Delete message on warn</label>
                <label for="deleting_reason">Reason:</label>
                <input type="text" name="deleting_reason" id="">
                <input type="submit" value="Warn">
            </form>
            <button id="closeFormFrame">Close form</button>
            `)

        $("#is_deleted").click(function(){
            if(this.checked){
                $("#deleting_reason").removeAttr("readonly")
            }
            else{$("#deleting_reason").attr("readonly", true) }
        })
        $("#closeFormFrame").click(function(){
            $("#warnForm").remove()
            this.remove()
        })
        })
    })
    
    // edit btn
    $(".editBtn").each(function(index, button){
        let msg = this.parentElement.parentElement.parentElement.lastElementChild.innerHTML;
        let id = this.parentElement.parentElement.parentElement.parentElement.getAttribute("id");
        this.addEventListener('click', function(){
            $("body").append(`
            <form action="/forum/message/${id}/edit/" id="editForm" method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                <label for="new_msg">Edit message: </label>
                <textarea name="new_msg" id="" cols="30" rows="5">${msg}</textarea>
                <label for="is_notified">Notify user:</label>
                <input type="checkbox" name="is_notified" id="">
                <label for="notification">Notification: </label>
                <input type="text" name="notification" id="">
                <input type="submit" value="Save">
            </form>
            <button id="closeFormFrame">Close form</button>
            `)

            $("#closeFormFrame").click(function(){
                $("#editForm").remove()
                this.remove()
            })
        })
    })


    // delete btn
    $(".delBtn").each(function(index, button){
        let msg = this.parentElement.parentElement.parentElement.lastElementChild.innerHTML;
        let id = this.parentElement.parentElement.parentElement.parentElement.getAttribute("id");
        this.addEventListener('click', function(){
            $("body").append(`
            <form action="/forum/message/${id}/delete/" method="post" id="deleteForm">
                <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                <label for="reason">Reason:</label>
                <input type="text" name="reason" id="">
                <label for="is_notified">Notify user</label>
                <input type="checkbox" name="is_notified" id="is_deleted">
                <label for="notification">Notification:</label>
                <input type="text" name="notification" id="deleting_reason" readonly>
                <input type="submit" value="Delete">
                <button id="closeFormFrame">Close form</button>
            </form>
            `)
            
            $("#is_deleted").click(function(){
                if(this.checked){
                    $("#deleting_reason").removeAttr("readonly")
                }
                else{$("#deleting_reason").attr("readonly", true) }
            })
            $("#closeFormFrame").click(function(){
                $("#deleteForm").remove()
                this.remove()
            })
        })
    })

    //view message btn
    $(".viewBtn").each(function(index, button){
        let id = this.parentElement.parentElement.parentElement.parentElement.getAttribute("id");
        this.addEventListener('click', function(){
            if($(`#msg_${id}`).attr("style"))
            {
                this.innerHTML = "Hide message"
                $(`#msg_${id}`).removeAttr("style")
            }
            else{
                this.innerHTML = "View message"
                $(`#msg_${id}`).attr("style", "display: none;")
            }
        })
    })
});

function GetCsrfToken()
{
    csrf = $("#token").attr("value");
    return csrf
}