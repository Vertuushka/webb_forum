$(document).ready(function() {
    let isMobile = false;
    let isMinimized = false;
    
    function onWindowResize() {
        let clientWidth = window.innerWidth;

        if (clientWidth <= 512) {
            isMobile = true;
        } else {
            isMobile = false;
        }

        console.log(isMobile);
        console.log(clientWidth);
    }

    $('#minimizeBtn').click(function() {
        $('#navConMain').slideToggle();
        $('#navConOptions').slideToggle();
    })

    onWindowResize();
    window.addEventListener('resize', onWindowResize);
});
