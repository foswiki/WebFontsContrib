"use strict";
jQuery(function($) {
   var timer,
      $overview = $(".overview"),
      $counter = $(".iconCount");

   function filterOverview(val) {
      var regex = new RegExp(val, "i"), count;

      if (val === '') {
         count = $overview.find(".entry").show().length;
      } else {
         count = $overview.find(".entry").hide().filter(function() {
            return regex.test($(this).text());
         }).show().length;
      }
      $counter.text(count);
   }
   $(".filterIcons").on("search", function() {
      var $input = $(this);
      if (typeof(timer) !== 'undefined') {
         window.clearTimeout(timer);
      }
      timer = window.setTimeout(function() {
         var val = $input.val();
         filterOverview(val);
         timer = undefined;
      }, 250);
   });
   filterOverview();
});