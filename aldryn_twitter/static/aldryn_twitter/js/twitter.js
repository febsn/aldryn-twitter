(function($) {
    function init() {
        var plugin_twitter = $(this);
        var tweet_container = plugin_twitter.find('.twitter-container');

        var options = {
            username: plugin_twitter.attr('data-username'),
            count: plugin_twitter.attr('data-count'),
            avatar_size: 32,
            join_text: 'auto',
            template: '{avatar}{time} {text}'
        };

        if (plugin_twitter.attr('data-query')) {
            options.query = plugin_twitter.attr('data-query');
        }

        tweet_container.tweet(options);
    }

    $(document).ready(function () {
        $('.plugin-twitter').each(init);
    });
})(jQuery);
