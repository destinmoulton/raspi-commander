(function() {
    "use strict";

    let currentCount = 0;

    window.onload = function() {
        addCSS("res/raspicommander.css");
        addModalElement();

        addScriptButtonListeners();
        setInterval(function() {
            // Check whether the scroll needs to change
            hasSTDOUTChanged();
        }, 100);
    };

    function addModalElement() {
        const modal = document.createElement("div");
        modal.setAttribute("class", "modal");

        const loadingAnimation = document.createElement("div");
        loadingAnimation.setAttribute("class", "loading-animation");
        modal.appendChild(loadingAnimation);

        document.body.appendChild(modal);
    }

    function toggleLoadingModal(state) {
        const className = state ? "loading" : "";
        document.body.setAttribute("class", className);
    }

    function addScriptButtonListeners() {
        const buttons = document.getElementsByClassName("script-run-button");
        for (let button of buttons) {
            button.addEventListener("click", handleScriptButtonClick);
        }
    }

    function handleScriptButtonClick(evt) {
        // Show the loading modal
        toggleLoadingModal(true);
    }

    function addCSS(fileName) {
        const css = document.createElement("link");
        css.setAttribute("rel", "stylesheet");
        css.setAttribute("type", "text/css");
        css.setAttribute("href", fileName);

        document.head.appendChild(css);
    }

    function hasSTDOUTChanged() {
        const el = document.getElementById("stdoutlist");
        const count = el.children.length;
        if (count !== currentCount) {
            // The number of children changed, so scroll
            currentCount = count;
            scroll(el);

            // Close the loading modal
            toggleLoadingModal(false);
        }
    }

    function scroll(element) {
        element.scrollTop = element.scrollHeight - element.clientHeight;
    }
})();
