$(document).ready(function() {
    console.log("123")
    function onWindowResize() {
        $('body').css('height', `${window.innerHeight}px`)
    }

    onWindowResize();
    window.addEventListener('resize', onWindowResize);

    // warning btn
    console.log($(".warnBtn"))
    $(".warnBtn").each(function(index, button){
        console.log("1")
        let msg = this.parentElement.parentElement.parentElement.lastElementChild.innerHTML;
        let id = this.parentElement.parentElement.parentElement.parentElement.getAttribute("id");
        this.addEventListener('click', function(){
            console.log(msg)
            $("body").append(`
            <form action="/forum/message/${id}/warn/" method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="${GetCsrfToken()}">
                <input type="text" name="warn_reason" id="">
                <label for=""><input type="checkbox" name="is_deleted" id="is_deleted">Delete message on warn</label>
                <input type="text" name="deleting_reason" id="deleting_reason" readonly>
                <input type="submit" value="Warn">
            </form>
            `)

        $("#is_deleted").click(function(){
            if(this.checked){
                $("#deleting_reason").removeAttr("readonly")
            }
            else{$("#deleting_reason").attr("readonly", true) }
        })
        })
    })
    
    // edit btn

    // delete btn

});

function GetCsrfToken()
{
    csrf = $("#token").attr("value");
    return csrf
}