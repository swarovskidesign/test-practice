$(document).ready(function() {

    $('#createwallet').submit(function(event) {
        event.preventDefault();

        $.ajax({
            url: '/operations/createwallet/',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert('Wallet created successfully!');
                $('#modal').hide();
                window.location.reload();
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);
            }
        });
    });

    $('#send').submit(function(event) {
        event.preventDefault();

        $.ajax({
            url: '/operations/send/',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert('Amount sent successfully!');
                $('#sendModal').hide();
            },
            error: function(xhr, status, error) {5
                alert('Error: ' + error);
            }
        });
    });

    $('#betweenForm').submit(function(event) {
        event.preventDefault();

        $.ajax({
            url: '/operations/between/',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert('Exchange successful!');
                $('#betweenModal').hide(); // Скрыть модальное окно
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);
            }
        });
    });

    $('#exchangeForm').submit(function(event) {
        event.preventDefault();

        $.ajax({
            url: '/operations/exchange/',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                alert('Exchange successful!');
                $('#exchangeModal').hide();
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);
            }
        });
    });

});