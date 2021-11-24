!(function (e) {
  "use strict";
  var a = function () {
    this.$realData = [];
  };
  (a.prototype.createBarChart = function (e, a, r, t, o, i) {
    Morris.Bar({
      element: e,
      data: a,
      xkey: r,
      ykeys: t,
      labels: o,
      hideHover: "auto",
      resize: !0,
      gridLineColor: "rgba(173, 181, 189, 0.1)",
      barSizeRatio: 0.2,
      dataLabels: !1,
      barColors: i,
    });
  }),
    (a.prototype.createLineChart = function (e, a, r, t, o, i, n, l, s) {
      Morris.Line({
        element: e,
        data: a,
        xkey: r,
        ykeys: t,
        labels: o,
        fillOpacity: i,
        pointFillColors: n,
        pointStrokeColors: l,
        behaveLikeLine: !0,
        gridLineColor: "rgba(173, 181, 189, 0.1)",
        hideHover: "auto",
        resize: !0,
        pointSize: 0,
        dataLabels: !1,
        lineColors: s,
      });
    }),
    (a.prototype.createDonutChart = function (e, a, r) {
      Morris.Donut({
        element: e,
        data: a,
        resize: !0,
        colors: r,
        backgroundColor: "transparent",
      });
    }),
    (a.prototype.init = function () {
      this.createBarChart(
        "morris-bar-example",
        [
          { y: "2012", a: 0 },
          { y: "2013", a: 25 },
          { y: "2014", a: 60 },
          { y: "2015", a: 40 },
          { y: "2016", a: 55 },
          { y: "2017", a: 50 },
          { y: "2018", a: 75 },
          { y: "2019", a: 38 },
          { y: "2020", a: 19 },
          { y: "2021", a: 93 },
        ],
        "y",
        ["a"],
        ["Statistics"],
        ["#188ae2"]
      );
      this.createLineChart(
        "morris-line-example",
        [
          { y: "2012", a: 0, b: 0 },
          { y: "2013", a: 50, b: 25 },
          { y: "2014", a: 75, b: 50 },
          { y: "2015", a: 30, b: 80 },
          { y: "2016", a: 50, b: 50 },
          { y: "2018", a: 75, b: 10 },
          { y: "2019", a: 50, b: 40 },
          { y: "2020", a: 75, b: 50 },
          { y: "2021", a: 100, b: 70 },
        ],
        "y",
        ["a", "b"],
        ["Series A", "Series B"],
        ["0.9"],
        ["#ffffff"],
        ["#999999"],
        ["#10c469", "#188ae2"]
      );
      this.createDonutChart(
        "morris-donut-example",
        [
          { label: "Total visit", value: 800 },
          { label: "Totel pending", value: 500 },
          { label: "Totel completed", value: 300 },
        ],
        ["#ff8acc", "#5b69bc", "#35b8e0"]
      );
    }),
    (e.Dashboard1 = new a()),
    (e.Dashboard1.Constructor = a);
})(window.jQuery),
  (function (e) {
    "use strict";
    window.jQuery.Dashboard1.init();
  })();
