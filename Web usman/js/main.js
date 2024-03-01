var tabButtons = document.querySelectorAll(".container .header2 button");
var tabPanels = document.querySelectorAll(".container .txt");

function showPanel(panelIndex,colorCode){
    tabButtons.forEach(function(node){
        node.style.background="";
        node.style.color = "";
    });
    tabButtons[panelIndex].style.backgroundColor=colorCode;
    tabButtons[panelIndex].style.color = "black";
    tabPanels.forEach(function(node){
        node.style.display = "none"
    });
    tabPanels[panelIndex].style.display = "block";
    tabPanels[panelIndex].style.backgroundColor = "colorCode"
}
showPanel(0,'#f44336')