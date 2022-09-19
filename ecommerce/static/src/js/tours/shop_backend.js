odoo.define("ecommerce.tour_shop_backend", function (require) {
    "use strict";

    var tour = require("web_tour.tour");
    var steps = require("ecommerce.tour_shop");
    tour.register("shop", {url: "/shop"}, steps);

});
