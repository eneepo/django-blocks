$(document).ready(function(){
    $('.block-wrapper.invisible').each(function() {
        var $this           = $('.block-wrapper.invisible'),
            blockId        = $this.attr('id'),
            retrievedBlockOptions   = localStorage.getItem(blockId);

        var blockOption = JSON.parse(retrievedBlockOptions);

        if(retrievedBlockOptions==null || blockOption['visible']==false){
            $this.removeClass('invisible');
        }

        $this.find('.alert-dismissible').on('close.bs.alert', function () {
            options = JSON.stringify({'visible':true})
            localStorage.setItem(blockId, options);
        })
    });

})
