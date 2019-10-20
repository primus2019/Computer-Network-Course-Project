<template>
  <div class="container">
    <h1>
      {{ message }}
    </h1>
    <button type="button"
            class="btn btn-primary"
            v-b-modal.login-modal>
            login
    </button>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">subject</th>
          <th scope="col">sender</th>
          <th scope="col">date</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(mail, index) in mails" :key="index">
          <td>{{ mail.subject }}</td>
          <td>{{ mail.sender }}</td>
          <td>{{ mail.date }}</td>
        </tr>
      </tbody>
    </table>
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">account</th>
          <th scope="col">password</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ newAccount.account }}</td>
          <td>{{ newAccount.password }}</td>
        </tr>
      </tbody>
    </table>
    <b-modal ref="accountLogin"
                id="login-modal"
                title="Login"
                hide-footer>
        <b-form @submit="onLogin" @reset="onReset" class="w-100">
            <b-form-group id="form-account-group"
                            label="账号:"
                            label-for="form-account-input">
                <b-form-input id="form-account-input"
                                type="text"
                                v-model="newAccount.account"
                                required
                                placeholder="Enter account">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-password-group"
                            label="密码:"
                            label-for="form-password-input">
                <b-form-input id="form-password-input"
                                type="password"
                                v-model="newAccount.password"
                                required
                                placeholder="Enter password">
                </b-form-input>
            </b-form-group>
            <b-button-group>
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-button-group>
        </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
/* eslint linebreak-style: ["error", "windows"] */
export default {
  data() {
    return {
      message: 'no message',
      newAccount: {
        account: '',
        password: '',
      },
      mails: [
        // {
        //   account_id: '12345',
        //   subject: 'hello world',
        //   sender: 'world',
        //   eceiver: 'me',
        //   date: 'today',
        //   content: 'hello world',
        //   read: true,
        // },
      ],
      addMail: {
        subject: '',
        sender: '',
        receiver: '',
        date: '',
        content: '',
        read: true,
      },
      editMail: {
        id: '',
        sender: '',
        receiver: '',
        date: '',
        content: '',
        read: true,
      },
    };
  },
  methods: {
    // 3 get mails by account ID
    getMails(accountID) {
      const path = `http://localhost:5000/OneBox/${accountID}`;
      axios.get(path)
        .then((res) => {
          this.mails = res.data.mails;
          this.message = res.data.status;
          // for test
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        });
    },
    initAccount() {
      this.newAccount.account = '';
      this.newAccount.password = '';
    },
    // 1
    onLogin(evt) {
      evt.preventDefault();
      this.$refs.accountLogin.hide();
      const payload = {
        account: this.newAccount.account,
        password: this.newAccount.password,
      };
      this.addAccount(payload);
      // this.initAccount();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.accountLogin.hide();
      this.initAccount();
    },
    // 2 add account to server, get and send accountID to getMails
    addAccount(payload) {
      const path = 'http://localhost:5000/OneBox/accounts';
      axios.post(path, payload)
        .then((res) => {
          this.getMails(res.data.account_id);
          this.message = 'Account added!';
          // this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error)
          // this.getMails(payloadk)
        });
    },
    getPreset() {
      this.getMails('12345');
    },
  },
  created() {
    this.getPreset();
  },
};
</script>
