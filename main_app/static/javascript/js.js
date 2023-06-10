var elem = $('.tabs')
var options = {}
var instance = M.Tabs.init(elem, options);
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
});
