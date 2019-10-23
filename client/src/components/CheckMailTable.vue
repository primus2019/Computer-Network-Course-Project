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
                <tr v-for='(mail, index) in mails' :key='index'>
                    <td v-b-modal.check-mail-modal @click="changeindex(index); changemail();">{{ mail.Subject }}</td>
                    <td v-b-modal.check-mail-modal @click="changeindex(index); changemail();">{{ mail.From }}</td>
                    <td v-b-modal.check-mail-modal @click="changeindex(index); changemail();">{{ mail.Date }}</td>
                </tr>
            </tbody>
        </table>
        <b-modal ref='mailCheck' id='check-mail-modal' :title=clicked_mail.Subject hide-footer>
            <b-button-group>
                <b-button v-b-toggle.collapse-Date variant="date">Date</b-button>
                <b-button v-b-toggle.collapse-From variant="from">From</b-button>
                <b-button v-b-toggle.collapse-To variant="to">To</b-button>
            </b-button-group>
            <b-collapse id="collapse-Date" visible accordion="accordion-1">
                <b-card>{{ clicked_mail.Date }}</b-card>
            </b-collapse>
            <b-collapse id="collapse-From" visible accordion="accordion-1">
                <b-card>{{ clicked_mail.From }}</b-card>
            </b-collapse>
            <b-collapse id="collapse-To" visible accordion="accordion-1">
                <b-card>{{ clicked_mail.To }}</b-card>
            </b-collapse>
            <b-media>
                <template>
                    <div v-for='(content, index) in clicked_mail.contents' :key="index">
                        <span v-if="content.content_type === 'text/html'">
                            <span v-html=content.content></span>
                        </span>
                        <span v-else-if="content.content_type === 'text/plain'">
                            {{  content.content  }}
                        </span>
                        <h1 v-else>this is {{  content.content_type  }}!</h1>
                    </div>
                </template>
            </b-media>
            <!-- <b-media>
                <template v-slot:aside>
                <b-img blank blank-color='#ccc' width='64' alt='placeholder'></b-img>
                </template>

                <h5 class='mt-0'>Media Title</h5>
                <p>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
                </p>
                <p>
                Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                penatibus et magnis dis parturient montes, nascetur ridiculus mus.
                </p>

                <b-media>
                <template v-slot:aside>
                    <b-img blank blank-color='#ccc' width='64' alt='placeholder'></b-img>
                </template>

                <h5 class='mt-0'>Nested Media</h5>
                <p class='mb-0'>
                    Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in
                    faucibus.
                </p>
                </b-media>
            </b-media> -->
        </b-modal>
    </div>
</template>

<script>
export default {
    name: 'checkmailtable',
    props: ['mails'],
    data() {
        return {
            clicked_index: 1,
            clicked_mail: {}
        };
    },
    methods: {
        changeindex(index) {
            this.clicked_index = index;
        },
        changemail() {
            this.clicked_mail = this.mails[this.clicked_index];
        }
    }
};
</script>
