<template>
    <div>
        <!-- <b-pagination-nav no-page-detect :number-of-pages="mails.length / 10 + 1" :limit=10 @click="changePageIndex(index)"></b-pagination-nav> -->
        <b-button-toolbar key-nav aria-label="Toolbar with button groups">
            <b-button-group class="mx-1">
                <b-button variant="success">&laquo;</b-button>
                <b-button variant="success">&lsaquo;</b-button>
            </b-button-group>
            <b-button-group class="mx-1">
                <div v-for='(mail, index) in mails' :key='index'>
                    <b-button variant="info" v-if='index % 10 === 0' @click="changePageIndex(index)">
                        {{ index / 10 + 1 }}
                    </b-button>
                </div>
            </b-button-group>
            <b-button-group class="mx-1">
                <b-button variant="success">&rsaquo;</b-button>
                <b-button variant="success">&raquo;</b-button>
            </b-button-group>
        </b-button-toolbar>
    </div>
</template>

<script>
export default {
    name: 'pagebar',
    props: ['mails'],
    data() {
        return {
            clicked_page_index: 0
        };
    },
    methods: {
        changePageIndex(index) {
            this.clicked_page_index = index / 10;
            this.$emit('input', this.clicked_page_index);
            // this.clicked_page_index = index;
            // this.$emit('input', this.clicked_page_index);
        }
    }
};
</script>
