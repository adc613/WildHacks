$(document).ready(function(){

    $('.up_vote').click(function(){
        var i = $(this).val(); 
        var url = '/ideas/upvote/' + i;
        var $vote = $('#votes_' + i); 

        $.ajax({
            type: 'GET',
            url: url,
            data: {},
            success : upVote($vote)
        });

    });

    $('.down_vote').click(function(){
        var i = $(this).val(); 
        var $vote = $('#votes_' + i); 
        var url = '/ideas/downvote/' + i;

        $.ajax({
            type: 'GET',
            url: url,
            data: {},
            success : downVote($vote)
        });

    });

    var upVote = function($vote){
        var i = parseInt($vote.text(), 10) + 1;
        $vote.text(i);
    };

    var downVote = function($vote){
        var i = parseInt($vote.text(), 10) - 1;
        $vote.text(i);
    };
});
