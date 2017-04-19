<script>
        hue = $("#confidence-meter").attr("value")*1.2;
        color = "background-color: hsl(" + hue + ", 75%, 48%)";
	      $("#confidence-meter").attr("style", color);
</script>
