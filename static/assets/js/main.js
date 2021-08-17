const autoHeight = () => {

    let elem = document.getElementById('elem');
    let elemChildren = elem.children;
    let elemMaxHeight = 0;
    let elemArray = new Array;

    Array.prototype.forEach.call(elemChildren, function (elemChild) {

        elemChild.style.height = '';

        elemArray.push(elemChild.clientHeight);

    });

    elemMaxHeight = Math.max.apply(null, elemArray);

    Array.prototype.forEach.call(elemChildren, function (elemChild) {

        elemChild.style.height = elemMaxHeight + 'px';

    });
}

window.addEventListener('load', autoHeight);
window.addEventListener('resize', autoHeight);
