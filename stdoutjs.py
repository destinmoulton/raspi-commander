STDOUTJS = """

function scroll(id){
    var element = document.getElementById(id);
    element.scrollTop = element.scrollHeight - element.clientHeight; 
    console.log("Scrolling...", id);
}
"""
