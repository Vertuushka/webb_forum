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
            <form class="popupContainer" action="/forum/message/${id}/warn/" method="post" id="warnForm">
                <div class="popup">
                    <h2 class="popupHeaderTitle">Create warning</h2>
                    <div class="cardLine"></div>
                    <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">

                    <div class="container cardSection">
                        <label class="meta" for="warn_reason">Warning reason:</label>
                        <input class="popupInput" type="text" name="warn_reason" id="">
                    </div>

                    <div class="cardLine"></div>
                    <div class="wrapper cardSection">
                        <input type="checkbox" name="is_deleted" id="is_deleted">
                        <label class="meta" for="">Delete message on warn</label>
                    </div>

                    <div class="container cardSection">
                        <label class="meta" for="deleting_reason">Reason:</label>
                        <input class="popupInput" type="text" name="deleting_reason" id="deleting_reason" readonly>
                    </div>

                    <div class="wrapper popupBtnWrapper">
                        <button class="popupBtn" id="closeFormFrame">Close form</button>
                        <button class="popupBtn popupActionBtn" type="submit">Warn</button>
                    </div>
                </div>
            </form>
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

    //thread del form
    $(".delete_thread_btn").each(function(index, button){
        let id = this.getAttribute("id");
        this.addEventListener('click', function(){
            $("body").append(`
            <form action="/forum/thread/${id}/delete/" method="post" id="thread_del_frame">
                <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                <input type="text" name="reason" id="">
                <input type="checkbox" name="is_notified" id="is_notified">
                <input type="text" name="notification" id="notification" readonly>
                <input type="submit" value="delete">
            </form>
            <button id="closeFormFrame">Cancel</button>
            `)
            $("#closeFormFrame").click(function(){
                $("#thread_del_frame").remove()
                this.remove()
            })
            $("#is_notified").click(function(){
                if(this.checked){
                    $("#notification").removeAttr("readonly")
                }
                else{$("#notification").attr("readonly", true) }
            })
        })
    })

    //restore thread btn
    $(".recycle").each(function(index, button){
        let id = this.getAttribute("id");
        this.addEventListener("click", function(){
            $("body").append(`
            <div id="restore_thread_frame">
                <p>You sure you want to restore this thread?</p>
                <a href="/forum/thread/${id}/delete/">Yes, restore</a>
                <button id="closeFormFrame">Cancel</button>
            </div>
            `)
            $("#closeFormFrame").click(function(){
                $("#restore_thread_frame").remove()
                this.remove()
            })
        })
    })

    //change thread form
    $(".editThreadBtn").each(function(index, button){
        let id_el = $(".thread_title");
        let id = id_el.attr("id");
        let is_delete = ($("#original_title").length > 0)
        if (is_delete) {
            console.log(true)
            var title_name = $("#original_title").attr("id");
        } 
        else {
            console.log(false)
            var title_name = document.querySelector(".thread_title").innerHTML;
        }
        this.addEventListener('click', function(){
            $("body").append(`
            <form action="/forum/thread/${id}/change/" method="post" id="change_thread_frame">
                <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                <input type="text" name="title" id="title" value="${title_name}">
                <label for="is_notified">Notify user:</label>
                <input type="checkbox" name="is_notified" id="is_notified">
                <input type="text" name="notification" id="notification" readonly>
                <input type="submit" value="Change">
            </form>
            <button id="closeFormFrame">Cancel</button>
            `)
            $("#closeFormFrame").click(function(){
                $("#change_thread_frame").remove()
                this.remove()
            })
            $("#is_notified").click(function(){
                if(this.checked){
                    $("#notification").removeAttr("readonly")
                }
                else{$("#notification").attr("readonly", true) }
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