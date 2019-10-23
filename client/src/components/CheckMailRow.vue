<template>
    <div class="checkmailrow">
        <tr v-for='(mail, index) in mails' :key='index'>
            <td v-b-modal.check-mail-modal >{{ mail.Subject }}</td>
            <td v-b-modal.check-mail-modal>{{ mail.From }}</td>
            <td v-b-modal.check-mail-modal>{{ mail.Date }}</td>
        </tr>
        <b-modal ref='mailCheck' id='check-mail-modal' title=' mail.Subject ' hide-footer>
            <b-media>
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
            </b-media>
        </b-modal>
    </div>
</template>

<script>
import checkmail from './CheckMail.vue';

export default {
    name: 'checkmailrow',
    props: ['mails']
    // components: {
    //     checkmail
    // }
};
</script>
