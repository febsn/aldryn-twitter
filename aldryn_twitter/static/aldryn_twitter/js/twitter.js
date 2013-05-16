(function($) {
    function init() {
        var plugin_twitter = $(this);
        var tweet_container = plugin_twitter.find('.twitter-container');

        var options = {
            username: plugin_twitter.attr('data-username'),
            count: plugin_twitter.attr('data-count'),
            avatar_size: 32,
            join_text: 'auto',
            auto_join_text_default: plugin_twitter.attr('data-trans-default'),
            auto_join_text_ed: plugin_twitter.attr('data-trans-ed'),
            auto_join_text_ing: plugin_twitter.attr('data-trans-ing'),
            auto_join_text_reply: plugin_twitter.attr('data-trans-reply'),
            auto_join_text_url: plugin_twitter.attr('data-trans-url'),
            loading_text: plugin_twitter.attr('data-trans-loading')
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
