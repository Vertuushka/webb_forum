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
            $(`#msg_${id}`).slideToggle("slow");
            if(this.innerHTML == "View message")
                this.innerHTML = "Hide message";
            else this.innerHTML = "View message";
              
        })
    })

    //view warn btn
    $(".viewWarn").each(function(index, button) {
        let baseUrl = window.location.protocol + "//" + window.location.host;
        let id = this.parentElement.parentElement.parentElement.parentElement.getAttribute("id");
        this.addEventListener('click', function() {
            $.get(`${baseUrl}/api.msg_warning/${id}/`, function(data) {
                console.log(data);
                $("body").append(`
                <div id="warning_info_frame">
                    <p>Warning info:</p>
                    <a href="/forum/${data.message.node_slug}/${data.message.thread_slug}.${data.message.thread_id}/#${data.message.id}">Message in ${data.message.thread_title}</a>
                    <img src="/${data.warned_by.profile_picture}" alt="">
                    <p>Warned by: <a href="/profile/${data.warned_by.id}/">${data.warned_by.username}</a></p>
                    <p>${data.details}</p>
                    <p>${data.time_warned}</p>
                    <button id="closeFormFrame">Close</button>
                </div>
                `)
                $("#closeFormFrame").click(function(){
                    $("#warning_info_frame").remove()
                    $("#warning_info_frame").remove()
                })
            });
        });
    });

    //report form
    $(".reportBtn").each(function(index, button){
        let id = this.parentElement.parentElement.parentElement.parentElement.getAttribute("id");
        this.addEventListener('click', function(){
            $("body").append(`
            <form action="/forum/message/${id}/report/" id="report_frame" method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                <input type="text" name="reason" id="" required>
                <input type="submit" value="Report">
            </form>
            <button id="closeFormFrame">Cancel</button>
            `)
            $("#closeFormFrame").click(function(){
                $("#report_frame").remove()
                this.remove()
            })
        })
    })

    //ban btn
    $(".banBtn").each(function(index, button){
        let userId = this.getAttribute("id")
        this.addEventListener('click', function(){
            $("body").append(`
            <form action="/profile/${userId}/ban/" method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                <label for="reason">Reason: </label>
                <input type="text" name="reason" id="">
                <label for="confirm_box">You sure you want to ban ${$("#username").text()}? User will not be able to use the forum on this account.</label>
                <input type="checkbox" name="confirm_box" id="_confirm_box">
                <input type="submit" value="Ban" id="banBtn" disabled>
            </form>
            `)
            $("#_confirm_box").click(function(){
                console.log(this)
                if(this.checked){
                    $("#banBtn").removeAttr("disabled")
                }
                else{$("#banBtn").attr("disabled", true) }
            })
            
        })
    })

    //report details form input stuff
    $("#is_notified").click(function(){
        if(this.checked){
            $("#notification").removeAttr("readonly")
        }
        else{$("#notification").attr("readonly", true) }
    })
    
    $("#threads_checkbox").click(function(){
        if(this.checked && $("#members_checkbox").prop("checked")){
            $("#members_checkbox").prop("checked", false)
        }
    })

    $("#members_checkbox").click(function(){
        if(this.checked && $("#threads_checkbox").prop("checked")){
            $("#threads_checkbox").prop("checked", false)
        }
    })
});

function GetCsrfToken()
{
    csrf = $("#token").attr("value");
    return csrf
}