<!-- eslint-disable -->
<!-- eslint comma-dangle: ["error", "never"] -->
<!-- eslint-disable-next-line vue/max-attributes-per-line -->
<!-- eslint-disable max-len -->
<!-- eslint-disable arrow-parens -->
<template>
  <div class='container'>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand>
        <h1>
          <b-badge variant="dark">One</b-badge>
          <b-badge variant="warning">Box</b-badge>
        </h1>
      </b-navbar-brand>
      <!-- <b-navbar-nav> -->
        <h4>
          <b-badge variant="light">Demo</b-badge>
        </h4>
      <!-- </b-navbar-nav> -->

      <b-navbar-toggle target="right-navbar"></b-navbar-toggle>

      <b-collapse id="right-navbar" is-nav>
        <b-navbar-nav class="ml-auto">
            <b-button variant="secondary" class='btn btn-primary' v-b-modal.send-modal :disabled=logined>send</b-button>
            <b-button variant="secondary" class='btn btn-primary' v-b-modal.login-modal>login</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <!-- <h2>{{ message }}</h2> -->
    <br>
    <pagebar :mails=mails v-model="clicked_page_index"></pagebar><br>
    <!-- <table class='table table-hover'>
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
          <checkmail v-b-modal.check-mail-modal :mail='mail'>{{ mail.Subject }}</checkmail>
          <td v-b-modal.check-mail-modal>{{ mail.From }}</td>
          <td v-b-modal.check-mail-modal>{{ mail.Date }}</td>
        </tr>
      </tbody>
      <checkmailrow :mails=mails></checkmailrow>
    </table> -->
    <checkmailtable :mails=mails :page_index=clicked_page_index></checkmailtable>
    <table class='table table-hover'>
      <thead>
        <tr>
          <th scope='col'>account</th>
          <th scope='col'>password</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ newAccount.account }}</td>
          <td>{{ newAccount.password }}</td>
        </tr>
      </tbody>
    </table>
    <b-modal ref='accountLogin' id='login-modal' title='Login' hide-footer>
      <b-form @submit='onLogin' @reset='onReset' class='w-100'>
        <b-form-group id='form-account-group' label='账号:' label-for='form-account-input'>
          <b-form-input
            id='form-account-input'
            type='text'
            v-model='newAccount.account'
            required
            placeholder='Enter account'
          ></b-form-input>
        </b-form-group>
        <b-form-group id='form-password-group' label='密码:' label-for='form-password-input'>
          <b-form-input
            id='form-password-input'
            type='password'
            v-model='newAccount.password'
            required
            placeholder='Enter password'
          ></b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type='submit' variant='primary'>Submit</b-button>
          <b-button type='reset' variant='danger'>Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref='sendMailModal' id='send-modal' title='Send new a letter' hide-footer>
      <b-form @submit='onSend' @reset='onDiscard' class='w-100'>
        <b-form-group id='form-to-group' label='To:' label-for='form-to-input'>
          <b-form-input
            id='form-to-input'
            type='text'
            v-model='newMail_To'
            required
            placeholder='Enter receivers'
          ></b-form-input>
        </b-form-group>
        <b-form-group id='form-subject-group' label='Subject:' label-for='form-subject-input'>
          <b-form-input
            id='form-subject-input'
            type='text'
            v-model='newMail_Subject'
            required
            placeholder='Enter subject'
          ></b-form-input>
        </b-form-group>
        <b-form-group id='form-text-group' label='Text:' label-for='form-text-input'>
          <b-form-textarea
            id="form-text-input"
            v-model="newMail_Text"
            required
            rows="3"
            max-rows="6"
            placeholder="Enter text content"
          ></b-form-textarea>
        </b-form-group>    
        <b-form-group id='form-application-group' label='File:' label-for='form-application-input'>
          <b-form-file
            id="form-application-input"
            v-model="newMail_Application"
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
    <b-modal ref="loading" hide-footer hide-header size='sm' body-bg-variant='primary' body-text-variant='light' centered>
        <b-button variant="primary" disabled>
            <b-spinner small type="grow"></b-spinner>
            Loading...
        </b-button>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
// import checkmail from './CheckMail.vue';
// import checkmailrow from './CheckMailRow.vue';
import checkmailtable from './CheckMailTable.vue';
import pagebar from './PageBar.vue';

/* eslint linebreak-style: ['error', 'windows'] */
export default {
  data() {
    return {
      message: 'no message',
      logined: true,
      clicked_page_index: 0,
      newAccount: {
        account: '',
        password: ''
      },
      newMail_To: '',
      newMail_Subject: '',
      newMail_Text: '',
      newMail_Application: null,
      account_id: '',
      mails: [
        {
          account_id: '12345',
          Subject: 'hello world',
          From: 'world',
          To: 'me',
          Date: 'today',
          contents: [
            {
                content_type: 'text/html',
                content: '<meta charset="UTF-8"/> <table align="center" style="font-family:Microsoft YaHei,Simsun;width:700px;table-layout:fixed;" bgcolor="#ffffff"        cellpadding="0" cellspacing="0">     <tbody>     <tr>         <td style="display:none;">\\xe7\\xbd\\x91\\xe6\\x98\\x93\\xe9\\x82\\xae\\xe7\\xae\\xb1\\xe5\\xa4\\xa7\\xe5\\xb8\\x88\\xe6\\xac\\xa2\\xe8\\xbf\\x8e\\xe4\\xbf\\xa1</td>     </tr>     <tr>         <td>             <table style="width:700px;" border="0" cellpadding="0" cellspacing="0">                 <tr>                     <td style="width:700px;height:375px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"><img                             src="https://mimg.127.net/hz/uploader/20171030/15093499095242237.jpg"                             style="display:block;border:0;"/></td>                 </tr>             </table>         </td>     </tr>     <tr>         <td>             <table style="width:700px;" border="0" cellpadding="0" cellspacing="0">                 <tr>                     <td rowspan="2"                         style="width:149px;height:153px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"></td>                     <td rowspan="2"                         style="width:170px;height:153px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"><img                             src="https://mimg.127.net/hz/uploader/20171031/15094146237198202.jpg"                             style="display:block;border:0;"/></td>                     <td style="width:230px;height:79px;font-family:Microsoft YaHei,Simsun;background:#fcf7ff;"><a                             style="display: block;" href="http://client.dl.126.net/pcmail/dashi/8/mail.exe"                             target="_blank"><img src="https://mimg.127.net/hz/uploader/20171031/15094146239508203.jpg"                                                  style="display:block;border:0;"/></a></td>                     <td rowspan="2"                         style="width:151px;height:153px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"></td>                 </tr>                 <tr>                     <td style="width:230px;height:74px;font-family:Microsoft YaHei,Simsun;background:#fcf7ff;"><a                             style="display: block;" href="http://client.dl.126.net/macmail/dashi/mailmaster.dmg"                             target="_blank"><img src="https://mimg.127.net/hz/uploader/20171031/15094146241488204.jpg"                                                  style="display:block;border:0;"/></a></td>                 </tr>             </table>         </td>     </tr>     <tr>         <td>             <table style="width:700px;" border="0" cellpadding="0" cellspacing="0">                 <tr>                     <td style="width:700px;height:812px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"><img                             src="https://mimg.127.net/hz/uploader/20171030/15093499106322241.jpg"                             style="display:block;border:0;"/></td>                 </tr>             </table>         </td>     </tr>     <tr>         <td>             <table style="width:700px;" border="0" cellpadding="0" cellspacing="0">                 <tr>                     <td style="width:700px;height:228px;font-family:Microsoft YaHei,Simsun;background:#ffffff;"><a style="display: block;"                                                                                                                    href="https://weibo.com/u/5252550107"                                                                                                                    target="_blank"><img                             src="http://mailshark.nos-jd.163yun.com/document/static/568BFCF0CC2B79A496421D588AD80CF5.png"                             style="display:block;border:0;"/></a></td>                 </tr>             </table>         </td>     </tr>     </tbody> </table>'
            }
        ],
          read: true
        }
      ],
      addMail: {
        subject: '',
        sender: '',
        receiver: '',
        date: '',
        content: '',
        read: true
      },
      editMail: {
        id: '',
        sender: '',
        receiver: '',
        date: '',
        content: '',
        read: true
      }
    };
  },
  components: {
    checkmailtable,
    pagebar
  },
  methods: {
    // 3 get mails by account ID
    getMails(accountID) {
      this.start_loading();
      const path = `http://localhost:5000/OneBox/${accountID}`;
      axios
        .get(path)
        .then((res) => {
          this.mails = res.data.mails;
          this.message = res.data.status;
          this.stop_loading();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    initAccount() {
      this.newAccount = {
        account: '',
        password: ''
      };
    },
    discardNewMail() {
      this.newMail_To = '';
      this.newMail_Subject = '';
      this.newMail_Text = '';
      this.newMail_Application = null;
    },
    // 1
    onLogin(evt) {
      this.start_loading();
      evt.preventDefault();
      this.$refs.accountLogin.hide();
      const payload = {
        account: this.newAccount.account,
        password: this.newAccount.password
      };
      this.addAccount(payload);
      // this.initAccount();
      this.logined = false;
      this.stop_loading();
    },
    onReset(evt) {
      this.start_loading();
      evt.preventDefault();
      this.$refs.accountLogin.hide();
      this.initAccount();
      this.stop_loading();
    },
    onSend(evt) {
      this.start_loading();
      evt.preventDefault();
      this.$refs.sendMailModal.hide();
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
        To: this.newMail_To,
        Subject: this.newMail_Subject,
        Text: this.newMail_Text,
        Application: this.newMail_Application
      };
      // console.log(this.newMail_Application);
      // console.log(payload.Application);
      // console.log(payload);
      this.sendMail(payload);
      this.stop_loading();
      this.discardNewMail();
    },
    onDiscard(evt) {
      this.start_loading();
      evt.preventDefault();
      this.$refs.sendMailModal.hide();
      this.discardNewMail();
      this.stop_loading();
    },
    // 2 add account to server, get and send accountID to getMails
    addAccount(payload) {
      this.start_loading();
      const path = 'http://localhost:5000/OneBox/accounts';
      axios
        .post(path, payload)
        .then((res) => {
          this.account_id = res.data.account_id;
          this.getMails(res.data.account_id);
          this.message = 'Account added!';
          // this.showMessage = true
          this.stop_loading();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          // this.getMails(payloadk)
        });
    },
    sendMail(payload) {
      this.start_loading();
      const path = `http://localhost:5000/OneBox/${this.account_id}`;
      axios
        .post(path, payload)
        .then(() => {
          this.messsage = 'Mail sent!';
          this.stop_loading();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getPreset() {
      this.getMails('12345');
    },
    start_loading() {
      this.$refs.loading.show();
    },
    stop_loading() {
      this.$refs.loading.hide();
    }
  },
  created() {
    this.getPreset();
    this.initAccount();
    this.discardNewMail();
  }
};
</script>
