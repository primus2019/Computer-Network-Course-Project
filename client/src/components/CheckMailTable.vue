<template>
    <div class="checkmailtable">
        <table class='table table-hover'>
            <thead>
                <tr>
                <th scope='col'>Subject</th>
                <th scope='col'>From</th>
                <th scope='col'>Date</th>
                <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for='(mail, index) in mails.slice(page_index*10, page_index*10+10)' :key='index'>
                    <td v-b-modal.check-mail-modal @click="changeindex(index+page_index*10); changemail();">{{ mail.Subject }}</td>
                    <td v-b-modal.check-mail-modal @click="changeindex(index+page_index*10); changemail();">{{ mail.From }}</td>
                    <td v-b-modal.check-mail-modal @click="changeindex(index+page_index*10); changemail();">{{ mail.Date }}</td>
                </tr>
            </tbody>
        </table>
        <b-modal
        scrollable
        size='xl'
        ref='mailCheck'
        id='check-mail-modal'
        :title=clicked_mail.Subject
        header-bg-variant='secondary'
        header-text-variant='light'
        footer-bg-variant='dark'
        >
            <b-nav tabs card-header>
                <b-nav-item v-b-toggle.collapse-Date variant="success">Date</b-nav-item>
                <b-nav-item v-b-toggle.collapse-From variant="info">From</b-nav-item>
                <b-nav-item v-b-toggle.collapse-To variant="warning"> To </b-nav-item>
            </b-nav>
            <b-collapse id="collapse-Date" visible accordion="accordion-1">
                <b-card>{{ clicked_mail.Date }}</b-card>
            </b-collapse>
            <b-collapse id="collapse-From" visible accordion="accordion-1">
                <b-card>{{ clicked_mail.From }}</b-card>
            </b-collapse>
            <b-collapse id="collapse-To" visible accordion="accordion-1">
                <b-card>{{ clicked_mail.To }}</b-card>
            </b-collapse>
            <!-- <b-dropdown id="dropdown-1" text="Dropdown Button" class="m-md-2">
                <div v-for='(content, index) in clicked_mail.contents' :key="index">
                    <b-dropdown-item href=index>{{  content.content_type  }}</b-dropdown-item>
                    <b-dropdown-divider></b-dropdown-divider>
                </div>
            </b-dropdown> -->
            <!-- further perfection: one collapse for one media and link the collapse with the dropdown to show one content at a time -->
            <b-media>
                <template>
                    <div v-for='(content, index) in clicked_mail.contents' :key="index">
                        <span v-if="content.content_type === 'text/html'">
                            <span v-html=content.content align-self='center'></span>
                        </span>
                        <span v-else-if="content.content_type === 'text/plain'">
                            <span v-html=content.content align-self='center'></span>
                        </span>
                        <downloadButton v-else-if="content.content_type === 'application/octet-stream'"
                        :content=content></downloadButton>
                        <h1 v-else>this is {{  content.content_type  }}!</h1>
                    </div>
                </template>
            </b-media>
            <template v-slot:modal-footer>
                <b-button @click="showReply()" block variant="dark" size='xl'>Reply</b-button>
            </template>
        </b-modal>
        <b-modal ref='replyMailModel' id='reply-modal' title='Reply' hide-footer>
            <b-form @submit='onSend' @reset='onDiscard' class='w-100'>
                <b-form-group id='form-to-group-reply' label='To:' label-for='form-to-input-reply'>
                <b-form-input
                    id='form-to-input-reply'
                    type='text'
                    v-model='replyMail_To'
                    required
                    placeholder='Enter receivers'
                ></b-form-input>
                </b-form-group>
                <b-form-group id='form-subject-group-reply' label='Subject:' label-for='form-subject-input-reply'>
                <b-form-input
                    id='form-subject-input-reply'
                    type='text'
                    v-model='replyMail_Subject'
                    required
                    placeholder='Enter subject'
                ></b-form-input>
                </b-form-group>
                <b-form-group id='form-text-group-reply' label='Text:' label-for='form-text-input-reply'>
                <b-form-textarea
                    id="form-text-input-reply"
                    v-model="replyMail_Text"
                    required
                    rows="3"
                    max-rows="6"
                    placeholder="Enter text content"
                ></b-form-textarea>
                </b-form-group>
                <b-form-group id='form-application-group-reply' label='File:' label-for='form-application-input-reply'>
                <b-form-file
                    id="form-application-input-reply"
                    v-model="replyMail_Application"
                    placeholder="Choose a file or drop it here..."
                    drop-placeholder="Drop file here..."
                ></b-form-file>
                </b-form-group>
                <!-- <template v-slot:modal-footer> -->
                    <b-button type='submit' variant='primary'>Send</b-button>
                    <b-button type='reset' variant='danger'>Discard</b-button>
                <!-- </template> -->
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';

import downloadButton from './DownloadButton.vue';

export default {
    name: 'checkmailtable',
    props: ['mails', 'page_index'],
    data() {
        return {
            clicked_index: 1,
            clicked_mail: {},
            replyMail_Subject: '',
            replyMail_To: '',
            replyMail_Text: '',
            replyMail_Application: null
        };
    },
    components: {
        downloadButton
    },
    methods: {
        changeindex(index) {
            this.clicked_index = index;
        },
        changemail() {
            this.clicked_mail = this.mails[this.clicked_index];
        },
        onSend(evt) {
            // this.start_loading();
            evt.preventDefault();
            this.$refs.replyMailModel.hide();
            // Application is a js File object
            // const reader = new FileReader();
            // // reader.onload = function (e) {};
            // reader.addEventListener('load', function () {
            //   this.newMail_Application = reader.result.toString();
            //   console.log(this.newMail_Application);
            // }, false);
            // reader.readAsDataURL(this.newMail_Application);
            // console.log(this.newMail_Application);
            const payload = {
                To: this.replyMail_To,
                Subject: this.replyMail_Subject,
                Text: this.replyMail_Text,
                Application: this.replyMail_Application
            };
            // console.log(this.newMail_Application);
            // console.log(payload.Application);
            // console.log(payload);
            this.replyMail(payload, this.clicked_mail.account_id, this.clicked_mail.id);
            // this.stop_loading();
            this.discardReplyMail();
        },
        onDiscard(evt) {
            // this.start_loading();
            evt.preventDefault();
            this.$refs.replyMailModel.hide();
            this.discardReplyMail();
            // this.stop_loading();
        },
        showReply() {
            this.$refs.replyMailModel.show();
        },
        discardReplyMail() {
            this.replyMail_Subject = '';
            this.replyMail_To = '';
            this.replyMail_Text = '';
            this.replyMail_Application = null;
        },
        replyMail(payload, account_id, mail_id) {
            // this.start_loading();
            const path = `http://localhost:5000/OneBox/${account_id}/${mail_id}`;
            axios
                .post(path, payload)
                .then(() => {
                this.messsage = 'Mail replied!';
                // this.stop_loading();
                })
                .catch((error) => {
                // eslint-disable-next-line
                console.log(error);
                });
        }
    }
};
</script>
