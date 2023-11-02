<script>
    // Initialize the toast
    var simpleToast = new bootstrap.Toast(document.getElementById('simpleToast'));

    // Show the toast when the button is clicked
    document.getElementById('showSimpleToastBtn').addEventListener('click', function () {
        simpleToast.show();
    });
</script>
