<template>
    <div>
        <!-- <b-pagination-nav no-page-detect :number-of-pages="mails.length / 10 + 1" :limit=10 @click="changePageIndex(index)"></b-pagination-nav> -->
        <b-button-toolbar key-nav aria-label="Toolbar with button groups">
            <b-button-group class="mx-1">
                <b-button variant="secondary" @click="set_smallest">&laquo;</b-button>
                <b-button variant="secondary" @click="set_smaller">&lsaquo;</b-button>
            </b-button-group>
            <b-button-group class="mx-1">
                <!-- <div v-for='(mail, index) in mails.slice(smallest_page_index * 10, (smallest_page_index + 10) * 10)' :v-bind="smallest_page_index" :key='index'> -->
                <div v-for='(mail, index) in mails_on_display' :key='index'>
                    <b-button variant="secondary" v-if='index % 10 === 0' @click="changePageIndex(index)">
                        {{ index / 10 + 1 + smallest_page_index }}
                    </b-button>
                </div>
            </b-button-group>
            <b-button-group class="mx-1">
                <b-button variant="secondary" @click="set_bigger">&rsaquo;</b-button>
                <b-button variant="secondary" @click="set_biggest">&raquo;</b-button>
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
            clicked_page_index: 0,
            smallest_page_index: 0,
            mails_on_display: null
        };
    },
    methods: {
        changePageIndex(index) {
            this.clicked_page_index = index / 10 + this.smallest_page_index;
            this.$emit('input', this.clicked_page_index);
        },
        set_smallest() {
            this.smallest_page_index = 0;
            this.update_mail_on_display();
        },
        set_smaller() {
            if (this.smallest_page_index > 0) {
                this.smallest_page_index = this.smallest_page_index - 1;
                this.update_mail_on_display();
            }
        },
        set_biggest() {
            this.smallest_page_index = Math.floor(this.mails.length / 10 - 10);
            this.update_mail_on_display();
        },
        set_bigger() {
            if (this.smallest_page_index < Math.floor(this.mails.length / 10 - 10)) {
                this.smallest_page_index = this.smallest_page_index + 1;
                this.update_mail_on_display();
            }
        },
        update_mail_on_display() {
            this.mails_on_display = this.mails.slice(this.smallest_page_index * 10, (this.smallest_page_index + 10) * 10);
            this.$forceUpdate();
            // console.log('update' + this.clicked_page_index);
        }
    },
    created() {
        this.mails_on_display = this.mails.slice(this.smallest_page_index * 10, (this.smallest_page_index + 10) * 10);
    }
};
</script>
