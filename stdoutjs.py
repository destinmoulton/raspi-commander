STDOUTJS = """
(function(){
    "use strict";

    let currentCount = 0;

    window.onload = function(){
        setInterval(function(){
            // Check whether the scroll needs to change
            shouldScroll();
        }, 100);
    }

    function shouldScroll(){
        const el = document.getElementById("stdoutlist")
        const count = el.children.length
        if(count !== currentCount){
            // The number of children changed, so scroll
            currentCount = count;
            scroll(el);
        }
    }

    function scroll(element){
        element.scrollTop = element.scrollHeight - element.clientHeight; 
    }
})()

"""
