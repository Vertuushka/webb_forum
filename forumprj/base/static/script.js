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
                        <label class="text" for="is_deleted">Delete message on warn</label>
                    </div>

                    <div class="container cardSection">
                        <label class="meta" for="deleting_reason">Reason:</label>
                        <input class="popupInput" type="text" name="deleting_reason" id="deleting_reason" readonly>
                    </div>

                    <div class="wrapper popupBtnWrapper">
                        <button class="popupBtn" id="closeFormFrame">Cancel</button>
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
            <form action="/forum/message/${id}/edit/" class="popupContainer" id="editForm" method="post">
                <div class="popup">
                    <h2 class="popupHeaderTitle">Edit message</h2>
                    <div class="cardLine"></div>
                    <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                

                    <div class="container cardSection">
                        <label for="new_msg" class="meta">Message</label>
                        <textarea name="new_msg" id="new_msg" class="popupInput">${msg}</textarea>
                    </div>

                    <div class="cardLine"></div>
                    <div class="cardSection wrapper">
                    <input type="checkbox" name="is_notified" id="is_notified" class="popupInput">
                        <label for="is_notified" class="text">Notify user</label>
                    </div>

                    <div class="container cardSection">
                        <label for="notification" class="meta">Notification</label>
                        <input type="text" name="notification" id="notification" class="popupInput" readonly>
                    </div>

                    <div class="wrapper popupBtnWrapper">
                        <button class="popupBtn" id="closeFormFrame">Cancel</button>
                        <button class="popupBtn popupActionBtn" type="submit">Save</button>
                    </div>
                </div>
            </form>
            `)

            $("#closeFormFrame").click(function(){
                $("#editForm").remove()
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


    // delete btn
    $(".delBtn").each(function(index, button){
        let msg = this.parentElement.parentElement.parentElement.lastElementChild.innerHTML;
        let id = this.parentElement.parentElement.parentElement.parentElement.getAttribute("id");
        this.addEventListener('click', function(){
            $("body").append(`
            <form action="/forum/message/${id}/delete/" class="popupContainer" id="deleteForm" method="post">
                <div class="popup">
                    <h2 class="popupHeaderTitle">Delete message</h2>
                    <div class="cardLine"></div>
                    <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                
            
                    <div class="container cardSection">
                        <label for="reason" class="meta">Reason</label>
                        <input type="text" name="reason" id="reason" class="popupInput">
                    </div>
            
                    <div class="cardLine"></div>
                    <div class="cardSection wrapper">
                    <input type="checkbox" name="is_notified" id="is_notified" class="popupInput">
                    <label for="is_notified" class="text">Notify user</label>
                    </div>
            
                    <div class="container cardSection">
                        <label for="notification" class="meta">Notification</label>
                        <input type="text" name="notification" id="notification" class="popupInput" readonly>
                    </div>
            
                    <div class="wrapper popupBtnWrapper">
                        <button class="popupBtn" id="closeFormFrame">Close form</button>
                        <button class="popupBtn popupActionBtn" type="submit">Delete</button>
                    </div>
                </div>
            </form>
            `)
            
            $("#is_notified").click(function(){
                if(this.checked){
                    $("#notification").removeAttr("readonly")
                }
                else{$("#notification").attr("readonly", true) }
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
                <div class="popupContainer" id="warning_info_frame">
                    <div class="popup">
                        <h2 class="popupHeaderTitle">Warning details</h2>
                        <div class="cardLine"></div>
                    
                        <div class="cardSection container">
                            <p class="meta">Message in "${data.message.thread_title}"</p>
                            <a href="/forum/${data.message.node_slug}/${data.message.thread_slug}.${data.message.thread_id}/#${data.message.id}" class="text">${data.message.message}</a>
                        </div>
                        <div class="cardSection container">
                            <p class="meta">Warned by</p>
                            <div class="wrapper cardSectionAutherItemMetaContainer">
                                <img src="/${data.warned_by.profile_picture}" alt="" class="themeCardSectionProfilePicture">
                                <a href="/profile/${data.warned_by.id}/" class="text">${data.warned_by.username}</a>
                            </div>
                        </div>
                        <div class="cardSection container">
                            <p class="meta">Details</p>
                            <p class="text">${data.details}</p>
                        </div>
                
                        <div class="cardLine"></div>
                        <div class="cardSection container">
                            <p class="meta">Time</p>
                            <p class="text">${data.time_warned}</p>
                        </div>
                        <div class="popupBtnWrapper wrapper">
                            <button id="closeFormFrame" class="popupBtn">Close</button>
                        </div>
                    </div>
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
            <form action="/forum/message/${id}/report/" class="popupContainer" id="report_frame" method="post">
                <div class="popup">
                    <h2 class="popupHeaderTitle">Report message</h2>
                    <div class="cardLine"></div>
                    <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                
                    <div class="container cardSection">
                        <label for="reason" class="meta">Reason</label>
                        <input type="text" name="reason" id="reason" class="popupInput">
                    </div>
                    <div class="wrapper popupBtnWrapper">
                        <button class="popupBtn" id="closeFormFrame">Cancel</button>
                        <button class="popupBtn popupActionBtn" type="submit">Report</button>
                    </div>
                </div>
            </form>
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
            if(this.innerHTML == "Unban") return
            $("body").append(`
            <form action="/profile/${userId}/ban/" class="popupContainer" id="userBanForm" method="post">
            <div class="popup">
                <h2 class="popupHeaderTitle">Ban ${$("#username").text()}</h2>
                <div class="cardLine"></div>
                <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
            
        
                <div class="container cardSection">
                    <label for="reason" class="meta">Reason</label>
                    <input type="text" name="reason" id="reason" class="popupInput">
                </div>
        
                <div class="cardLine"></div>
                <div class="cardSection container">
                    <p class="meta">Confirmation</p>
                    <div class="wrapper" style="gap: 8px;">
                        <input type="checkbox" name="confirm_box" id="confirm_ban_box" class="popupInput" required>
                        <label for="confirm_ban_box" class="text">You sure you want to ban ${$("#username").text()}? User will not be able to use the forum on this account.</label>
                    </div>
                </div>
        
                <div class="wrapper popupBtnWrapper">
                    <button class="popupBtn" id="closeFormFrame">Cancel</button>
                    <button class="popupBtn popupActionBtn" type="submit" id="banBtn">Ban</button>
                </div>
            </div>
        </form>
            `)
            $("#confirm_box").click(function(){
                // console.log(this)
                if(this.checked){
                    $("#banBtn").removeAttr("disabled")
                }
                else{$("#banBtn").attr("disabled", true) }
            })
            $("#closeFormFrame").click(function(){
                $("#userBanForm").remove()
                this.remove()
            })
        })
    })

    //thread del form
    $(".delete_thread_btn").each(function(index, button){
        let id = this.getAttribute("id");
        this.addEventListener('click', function(){
            $("body").append(`
            <form action="/forum/thread/${id}/delete/" class="popupContainer" id="thread_del_frame" method="post">
                <div class="popup">
                    <h2 class="popupHeaderTitle">Delete thread</h2>
                    <div class="cardLine"></div>
                    <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                

                    <div class="container cardSection">
                        <label for="reason" class="meta">Reason</label>
                        <input type="text" name="reason" id="reason" class="popupInput">
                    </div>

                    <div class="cardLine"></div>
                    <div class="cardSection wrapper">
                        <input type="checkbox" name="is_notified" id="is_notified" class="popupInput">
                        <label for="is_notified" class="text">Notify user</p>
                    </div>

                    <div class="container cardSection">
                        <label for="notification" class="meta">Notification</label>
                        <input type="text" name="notification" id="notification" class="popupInput" readonly>
                    </div>

                    <div class="wrapper popupBtnWrapper">
                        <button class="popupBtn" id="closeFormFrame">Cancel</button>
                        <button class="popupBtn popupActionBtn" type="submit">Delete</button>
                    </div>
                </div>
            </form>

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
            <div class="popupContainer" id="restore_thread_frame">
                <div class="popup">
                    <h2 class="popupHeaderTitle">Restore thread</h2>
                    <div class="cardLine"></div>
                
                    <div class="cardSection container">
                        <p class="meta">Confirmation</p>
                        <p class="text">You sure you want to restore this thread?</p>
                    </div>

                    <div class="wrapper popupBtnWrapper">
                        <button class="popupBtn" id="closeFormFrame">Cancel</button>
                        <button class="popupBtn popupActionBtn" type="submit"><a href="/forum/thread/${id}/delete/" class="text">Yes, restore</a></button>
                    </div>
                </div>
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
            <form action="/forum/thread/${id}/change/" class="popupContainer" id="change_thread_frame" method="post">
                <div class="popup">
                    <h2 class="popupHeaderTitle">Edit thread</h2>
                    <div class="cardLine"></div>
                    <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                
                    <div class="cardSection container">
                        <label for="title" class="meta">Thread title</label>
                        <input type="text" name="title" id="title" value="${title_name}"  class="popupInput">
                    </div>
            
                    <div class="cardLine"></div>
                    <div class="cardSection wrapper">
                        <input type="checkbox" name="is_notified" id="is_notified" class="popupInput">
                        <label for="is_notified" class="text">Notify user</label>
                    </div>
            
                    <div class="container cardSection">
                        <label for="notification" class="meta">Notification</label>
                        <input type="text" name="notification" id="notification" class="popupInput" readonly>
                    </div>
            
                    <div class="wrapper popupBtnWrapper">
                        <button class="popupBtn" id="closeFormFrame">Cancel</button>
                        <button class="popupBtn popupActionBtn" type="submit">Change</button>
                    </div>
                </div>
            </form>
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